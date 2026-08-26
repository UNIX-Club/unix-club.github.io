---
title: Choosing between LaTeX and Alternatives
author: Max Xu
date: 2026-08-25
tags: [LaTeX, productivity]
---

LaTeX is a typesetting system commonly used for technical writing, ranging from school assignments, research papers, and documentation.

## Why typeset notes and assignments?

Using a typesetting system makes your writing and notes more accessible:

- formulas and symbols are rendered cleanly and consistently
- the final PDF is easier to read and more professional
- text remains selectable and searchable, making it easier to review later
- collaboration is easier with cloud editors or version control

We briefly review several options and help you choose the best fit for your situation.

## LaTeX

Learning LaTeX can pay off immediately if you are taking math, science, or engineering courses. For example, some UofT courses, such as **MAT148/MAT149** and **MAT237**, use LaTeX templates or accept assignments as PDFs generated with LaTeX. Check the current course outline for the exact submission requirements.

### Local LaTeX

A local LaTeX installation gives you the most control, but it requires more setup. A typical setup includes:

- a TeX distribution, such as TeX Live, MiKTeX, or MacTeX
- a text editor or IDE
- a PDF viewer or preview tool
- build commands or a file watcher to compile `.tex` files into PDFs

Advantages of local LaTeX:
- it runs on your own machine and can use your local hardware (editing experience is fast and responsive)
- it works offline once installed
- you have full control over packages, templates, and compilation settings
- there are no cloud storage or account requirements

Trade-offs:

- setup can be less straightforward
- collaboration must be handled through external tools, such as Git
- must handle backups yourself

With a configurable text editor such as `nvim`, you can add useful tooling, including:

- snippets: automatically expand short text triggers into full blocks of LaTeX code with fillable placeholders
- autocomplete or completions: real-time suggestions that predict and fill in commands/filenames
- error checking: automated code analysis that detects syntax errors

We (the *NIX club) are happy to help if you run into any issues with your local LaTeX install.

### Overleaf

Overleaf is an online LaTeX editor. It combines a text editor, compiler, PDF viewer, and collaboration features in one web app. It is a convenient option if you do not want to set up a local LaTeX environment.

Advantages:

- no local installation required
- real-time collaboration is built in
- sharing, comments, and templates are easy to use
- it is a good fit when you need to submit a LaTeX-generated PDF without maintaining local tooling

Trade-offs:

- an internet connection is required
- your documents are stored online
- the free plan may have slower compilation and usage limits for larger projects
- collaborator limits may apply depending on the plan
- paid plans cost more and, as of writing, start around $20/mo, with student pricing around $10/mo; check current pricing
- if you need full control over your environment, a local setup or self-hosted Community Edition may be preferable

## Non-LaTeX Alternatives

The following tools are **not** LaTeX systems. They can be useful for notes, writing, or math rendering, but they will not satisfy a requirement to use a specific LaTeX template or compile a LaTeX document.

### Typst

Typst is a modern typesetting system with a simple syntax, fast compilation, and good math support. It is not LaTeX, so it should not be used if a course or journal requires a LaTeX template. It may be a good choice for personal documents or projects where LaTeX compatibility is not required.

### Obsidian

Obsidian is a local-first Markdown note-taking app with a large plugin ecosystem. It can render LaTeX-style equations and supports PDF export, depending on the export method and plugins.

A notable option is the [LaTeX Suite](https://community.obsidian.md/plugins/obsidian-latex-suite) plugin, which lets you use LaTeX-like equation syntax inside Markdown files and provides convenient keybindings or snippets.

Advantages:

- free and fully usable offline
- good for notes, linked documents, and personal knowledge management
- plugin ecosystem allows a lot of customization

Trade-offs:

- it is not a full typesetting system
- pages with many equations can lag, especially when equations are rendered as live objects
- does not handle collaboration
- must handle backups yourself

### Notion

Notion is a cloud-based workspace for documents, notes, databases, and collaboration. It supports inline and block LaTeX equations within an otherwise rich-text, Markdown-like environment. Its' cloud based nature facilitates collaboration.

## Summary

If a course or journal requires LaTeX, you should use **local LaTeX** or **Overleaf**.
- If you want the easiest LaTeX experience with collaboration, start with **Overleaf**.
- If you need full control, offline work, or custom packages, use **local LaTeX**.

If you are only intersted in keeping clean typeset notes, and want accessible options:
- If you do not need LaTeX compatibility and prefer a simpler modern typesetting syntax, consider **Typst**.
- If your goal is note-taking with some math support, consider **Obsidian** for offline work or **Notion** for collaboration.