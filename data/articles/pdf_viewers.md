---
title: PDF Viewers
author: Hyde Yoo
date: 2026-09-03
tags: [LaTeX, productivity]
---

PDFs (Portable Document Format) are used as the gold standard for documents, so a good PDF viewer is valuable.
For example, when typesetting documents with LaTeX, it is common to compile the document into a PDF file to preview the current progress. A good PDF viewer can offer useful features such as automatic reloading and jumping to text from PDF to editor (and vice versa).

In this article, we will introduce few popular PDF viewers that can complement your workflow.

## Web Browsers

| Windows | MacOS | GNU/Linux |
| ------- | ----- | --------- |
| ✔       | ✔     | ✔         |

Most major web browsers natively supports viewing and editing PDFs.

## [Firefox](https://www.firefox.com/)

Firefox's PDF viewer is actually mostly built with an independent JS library project, called [PDF.js](https://mozilla.github.io/pdf.js/).

PDF.js is the most popular open source PDF renderer as of 2026. It supports all features a basic PDF viewer requires, including

- Navigation (zoom, rotation, scrolling, thumbnails, bookmarks)
- Text search and selection
- Printing
- Basic annotations (viewing existing ones, plus a lightweight editor for free text, highlights, stamps, ink, and signatures)

However, it has some limitations:

- OCR
- Redaction
- Annotations with shapes, arrows, sticky notes, or measurement tools
- Digital signatures (only basic drawing, not certificate-based/verified signing)
- Office file support (Word, Excel, PowerPoint)
- Potential performance degradation for more complex PDFs

## [Chrome](https://www.google.com/chrome/)/[Chromium](https://www.chromium.org/Home/)

Chrome/Chromium's pdf viwer is based on [PDFium](https://pdfium.googlesource.com/pdfium/).

Few notable differences between chromium and firefox is that chromium has

- Better rendering performance and fidelity
- Form filling

### [Edge](https://explore.microsoft.com/)

Edge's pdf viwer builds on top of Chromium, with additional features such as

- Read aloud/text-to-speech
- Immersive reader
- Built-in translator

## [Adobe Acrobat](https://www.adobe.com/acrobat.html)

| Windows | MacOS | GNU/Linux |
| ------- | ----- | --------- |
| ✔       | ✔     | ✘         |

Adobe Acrobat is arguably the most popular PDF viewer out there. It is developed by the creator of PDF, Adobe Systems.

Acrobat is the most feature complete, to the point where some may say it's bloated. Unfortunately, many of its feature is hidden behind a _paywall_. Unless you have an active Adobe subscription, I wouldn't recommend Adobe unless you need a highly specific feature from it. A good example of this is signing government forms, where the specific format required by the government may only be supported by Acrobat.

## [Skim](https://skim-app.sourceforge.io/)

| Windows | MacOS | GNU/Linux |
| ------- | ----- | --------- |
| ✘       | ✔     | ✘         |

> Skim is a PDF reader and note-taker for OS X. It is designed to help you read and annotate scientific papers in PDF, but is also great for viewing any PDF file.

Skim's notable feature is its annotation workflow: it supports notes, highlighting, bookmarks, and viewing all annotations in one place. It also includes useful reading tools such as snapshots, a reading bar, smart cropping, and previews of internal links. It supports and integrates tools such as AppleScript, BibDesk, SyncTeX, and PDFSync, making it useful for automated, research-oriented, or LaTeX-based workflows.

## [Zathura](https://pwmt.org/projects/zathura/)

| Windows | MacOS | GNU/Linux |
| ------- | ----- | --------- |
| ✘       | ✘     | ✔         |

> Highly customizable and functional document viewer (plugin based). Supports PDF, DjVu, PostScript and Comicbook.

Zathura is primarily a document viewer and doesn't provide the editing features found in PDF editors. Its keybindings and configuration are inspired by vim, which makes it perfect for a keyboard-based workflow. Additionally, it supports automatic document reloading and bidirectional SyncTeX, making it particularly useful when typesetting documents with LaTeX. That is, the viewer will reload itself when it detects the currently open file changed (e.g. from recompiling a LaTeX document).

## [Sioyek](https://sioyek.info/)

| Windows | MacOS | GNU/Linux |
| ------- | ----- | --------- |
| ✔       | ✔     | ✔         |

> Sioyek is a PDF viewer with a focus on technical books and research papers.

Sioyek is another PDF viewer that has keybinds inspired by Vim similar to [Zathura](#Zathura). However, it has additional features such highlighting, portals, and smart jumps making navigation easier especially in larger documents.

## Closing thougts

There are many more PDF viwers that weren't mentioned in this article. Feel free to explore them.

If you are struggling to settle with one viewer, choose a random one and stick to it. You will get more comfortable with using it or eventually end up learning more about the features you care about.
