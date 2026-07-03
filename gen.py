import shutil
import re
from pathlib import Path

DATA_DIR = Path("data")
OUT_DIR = Path("out")

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

    output_content = MAIN_TEMPLATE.replace("{{BODY_SLOT}}", body_slot_content)
    output_content = output_content.replace("{{ROOT}}", root_prefix)
    output_content = output_content.replace("{{JS}}", js_content)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(output_content)
