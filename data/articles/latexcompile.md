---
title: Why LaTeX Compiles Twice
author: Max Xu
date: 2026-09-03
tags: [LaTeX]
---

A LaTeX distribution comes bundled with a lot of programs. Each program does one job, and they coordinate by leaving files on disk. That design explains two things people find odd: the pile of leftover auxiliary files, and why some documents need several compilations to come out right.

## Why the engine needs help

The engine reads your document once, front to back. When enough material has arrived to fill a page, it breaks the page and ships it into the PDF, and a shipped page is not revisited in the same pass. When it meets `\ref{intro}` on page 2 and the label is defined on page 40, it has nothing to print and no link target, giving the familiar `??` as a placeholder. It would be silly to only have backward references resolve on the first run, so no references are resolved at all in the first run.

Rather than teach the engine to backtrack, the design offloads the work to a later run. Every `\label` the engine encounters gets written to a side `.aux` file. That file is read back in at the start of the next compilation, so the numbers are already on hand. Most references therefore settle on the second pass.

## Why the table of contents needs more than one pass

The ToC lists page numbers, so it can't be built until they're settled; but the table of contents itself could be several pages long and sits at the front, so inserting it pushes those numbers down. Section titles and their pages go into a `.toc` file on the way through, and the same read-back trick breaks the cycle: each run typesets the contents from what the previous run measured.

A quick (albeit imprecise) high-level overview of the internals:

1. **Run one:** no `.toc` file yet, so the ToC comes out empty. The file is written.
2. **Run two:** the ToC appears at full length, shifting body page numbers. Run one's `.aux` is now stale, so references point at the wrong pages.
3. **Run three:** the shifted numbers are read back in and everything agrees. Usually it stops here, since the ToC's own length didn't change between runs two and three.

In rare situations, more passes are needed.

## Takeaways

- A run that fails partway can leave truncated auxiliary files, and every later run will faithfully read incorrect/broken info back in. They are best deleted.
- Keeping auxiliary files makes ordinary edits cheap. If no significant layout changes occur, references resolve in just one run.

Dealing with all of this by hand is quite painful, which is why `latexmk` exists. It automates the process of compiling a LaTeX document so you don't have to run a collection of obscure programs in an arcane order for your document to come out right.

<iframe src="https://skdoctool.maxxu.dev/files/6"></iframe>