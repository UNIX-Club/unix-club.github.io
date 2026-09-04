import html
import re
import shutil
from pathlib import Path

DATA_DIR = Path("data")
OUT_DIR = Path("out")

OUT_DIR.mkdir(parents=True, exist_ok=True)

with open("template/template.html", "r", encoding="utf-8") as f:
    MAIN_TEMPLATE = f.read()

FRONTMATTER_REGEX = re.compile(r"^---\n([\s\S]*?)\n---")

def parse_frontmatter(content):
    """Replicates JavaScript frontmatter parsing logic."""
    normalized_content = content.replace("\r\n", "\n")
    match = FRONTMATTER_REGEX.match(normalized_content)

    data = {}
    if not match:
        return data

    raw_yaml = match.group(1)
    for line in raw_yaml.split("\n"):
        parts = line.split(":")
        if len(parts) >= 2:
            key = parts[0].strip()
            value = ":".join(parts[1:]).strip()

            if value.startswith("[") and value.endswith("]"):
                value = [t.strip() for t in value[1:-1].split(",") if t.strip()]

            data[key] = value

    return data

def build_articles_page():
    articles = []
    articles_dir = DATA_DIR / "articles"

    if not articles_dir.exists():
        print("No articles directory found.")
        return

    # Find all markdown articles
    for file_path in articles_dir.rglob("*.md"):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        meta = parse_frontmatter(content)

        relative_path = file_path.relative_to(DATA_DIR).with_suffix(".html")
        url = f"./{relative_path.as_posix()}"

        title = meta.get("title", file_path.stem.replace("-", " ").title())
        date = meta.get("date", "Unknown Date")
        author = meta.get("author", "")
        tags = meta.get("tags", [])
        if isinstance(tags, str):
            tags = [tags] if tags else []

        articles.append({
            "title": title,
            "date": date,
            "author": author,
            "tags": tags,
            "url": url
        })

    articles.sort(key=lambda x: (x["date"] != "Unknown Date", x["date"]), reverse=True)

    articles_html = []

    articles_html.append('<h1 class="page-title">All Articles & Guides</h1>')
    articles_html.append('<div class="articles-container">')
    articles_html.append('  <div class="articles-grid">')

    for art in articles:
        title = html.escape(art["title"])
        author = html.escape(art["author"])
        date = html.escape(art["date"])
        url = html.escape(art["url"])
        tags = [html.escape(tag) for tag in art["tags"]]

        tags_html = ""
        if tags:
            tags_html = '<div class="article-tags">' + "".join(f'<span class="article-tag">#{tag}</span>' for tag in tags) + '</div>'

        meta_html = []
        if author:
            meta_html.append(f'<span>By <strong>{author}</strong></span>')
        if date and date != "Unknown Date":
            meta_html.append(f'<span>Published: {date}</span>')

        meta_str = f'<div class="article-meta">{" // ".join(meta_html)}</div>' if meta_html else ''

        card = f"""
        <div class="article-card">
            <h2 class="article-card-title"><a href="{url}">{title}</a></h2>
            <div class="article-card-footer">
                {meta_str}
                {tags_html}
            </div>
        </div>
        """
        articles_html.append(card)

    articles_html.append('  </div>')
    articles_html.append('</div>')

    body_content = "\n".join(articles_html)

    output_content = MAIN_TEMPLATE.replace("{{BODY_SLOT}}", body_content)
    output_content = output_content.replace("{{ROOT}}", "./")
    output_content = output_content.replace("{{JS}}", "")
    output_content = output_content.replace("{{TITLE}}", "Guides & Articles · UNIX-Club")

    with open(OUT_DIR / "articles.html", "w", encoding="utf-8") as f:
        f.write(output_content)

    print(f"Successfully generated articles.html with {len(articles)} items.")

if __name__ == "__main__":
    build_articles_page()
