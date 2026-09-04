# `UNIX-Club` Website

[![Website](https://github.com/UNIX-Club/unix-club.github.io/actions/workflows/deploy.yml/badge.svg)](https://github.com/UNIX-Club/unix-club.github.io/actions/workflows/deploy.yml)

A lightweight, minimal-dependency static site generator (SSG) system built for the `UNIX-Club` Website.

## Dependencies
- Python 3.x

## Project Structure
```
.
├── README.md               # This documentation file
├── build.sh                # Shell script wrapper to run the full site generation
├── data/                   # Raw content and source files
│   ├── articles/           # Markdown-based articles/guides
│   │   └── vim.md          # Sample article in markdown format
│   ├── index.md            # Site homepage source content
│   └── people.html         # Custom page layout written directly in HTML
├── scripts/                # Static site generation engine
│   ├── gen.py              # Main build engine for content-to-HTML conversion
│   └── gen_articles.py     # Index engine that dynamically builds the articles hub
└── template/               # Layout and behavior components
    ├── article.js          # JavaScript used in article subpages
    ├── default.js          # Default client-side JavaScript
    └── template.html       # Base HTML boilerplate with templating slots
```

## Building the Site
Run this at the project root:
```bash
chmod +x build.sh
./build.sh
```

## Adding Content
To add a general page:

Place the file inside the root of `data/`: Use `.html` if you want raw control over specific layout sections. Use `.md` for simple page bodies.

To add an article/guide:

All articles/guides go into `data/articles/`. Ensure your articles contain a valid YAML-like frontmatter metadata block. `gen_articles.py` will index it automatically.
