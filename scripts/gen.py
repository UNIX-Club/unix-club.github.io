import shutil
import re
from pathlib import Path

DATA_DIR = Path("data")
OUT_DIR = Path("out")
SITE_NAME = "UNIX-Club"

FRONTMATTER_REGEX = re.compile(r"^---\r?\n([\s\S]*?)\r?\n---")
H1_REGEX = re.compile(r"<h1[^>]*>([\s\S]*?)</h1>", re.IGNORECASE)


def frontmatter_title(content):
    match = FRONTMATTER_REGEX.match(content.replace("\r\n", "\n"))
    if not match:
        return None
    for line in match.group(1).split("\n"):
        parts = line.split(":")
        if len(parts) >= 2 and parts[0].strip() == "title":
            return ":".join(parts[1:]).strip()
    return None


def title_from_filename(stem):
    if stem.lower() == "index":
        return "Home"
    return stem.replace("-", " ").replace("_", " ").title()


def page_title(relative_path, file_ext, file_content):
    if file_ext == ".md":
        title = frontmatter_title(file_content)
        if title:
            return title
    elif file_ext == ".html":
        h1_match = H1_REGEX.search(file_content)
        if h1_match:
            return re.sub(r"\s+", " ", h1_match.group(1)).strip()
    return title_from_filename(relative_path.stem)


if OUT_DIR.exists():
    shutil.rmtree(OUT_DIR)
OUT_DIR.mkdir(parents=True, exist_ok=True)

with open("template/template.html", "r") as f:
    MAIN_TEMPLATE = f.read()

with open("template/default.js", "r") as f:
    DEFAULT_JS = f.read()

with open("template/article.js", "r") as f:
    ARTICLE = f.read()

# Supported file extensions for template processing
VALID_EXTENSIONS = {".md", ".html"}

for file_path in DATA_DIR.rglob("*"):
    if file_path.is_dir():
        continue

    relative_path = file_path.relative_to(DATA_DIR)
    file_ext = file_path.suffix.lower()

    # Static asset fallback (images, css, etc.)
    if file_ext not in VALID_EXTENSIONS:
        out_path = OUT_DIR / relative_path
        out_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(file_path, out_path)
        continue

    out_path = OUT_DIR / relative_path.with_suffix(".html")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    depth = len(relative_path.parent.parts)
    root_prefix = "../" * depth if depth > 0 else "./"

    if relative_path.parts and relative_path.parts[0] == "articles" and len(relative_path.parts) > 1:
        js_content = ARTICLE
    else:
        js_content = DEFAULT_JS

    with open(file_path, "r", encoding="utf-8") as f:
        file_content = f.read()

    if file_ext == ".md":
        body_slot_content = f'<script type="text/markdown" id="markdown-source">{file_content}</script>'
    elif file_ext == ".html":
        body_slot_content = file_content
        js_content = ""
    else:
        body_slot_content = "<p>Something went wrong.</p>"

    title = page_title(relative_path, file_ext, file_content)
    title_content = f"{title} · {SITE_NAME}" if title else SITE_NAME

    output_content = MAIN_TEMPLATE.replace("{{BODY_SLOT}}", body_slot_content)
    output_content = output_content.replace("{{ROOT}}", root_prefix)
    output_content = output_content.replace("{{JS}}", js_content)
    output_content = output_content.replace("{{TITLE}}", title_content)

    print(f"Generated {str(out_path)}")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(output_content)
