---
type: Guide
title: Open Knowledge Format in SMKB
description: The small OKF v0.2 conventions used for course notes in this template.
status: draft
generated: { by: Codex/gpt-6, at: 2026-11-02T02:55:52Z }
sources:
  - id: okf
    resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md
    title: Open Knowledge Format v0.2 specification
---

# Open Knowledge Format in SMKB

[Open Knowledge Format (OKF) v0.2](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md) describes a bundle of Markdown documents with YAML frontmatter. It does not prescribe course folder names. SMKB uses `references/` for source material and `lectures/`, `concepts/`, and `assignments/` for organized notes.[^okf]

## A knowledge page

Every knowledge Markdown page starts with `---` frontmatter. OKF requires only `type`; SMKB also asks agent-written pages for a clear title, one-sentence description, draft status, generating actor and UTC time, and sources for facts taken from other material.[^okf]

```md
---
type: Lecture
title: Lecture 1 — Least squares
description: Definitions and examples from the first regression lecture.
status: draft
generated: { by: "agent/model", at: "2026-11-02T18:00:00Z" }
sources:
  - id: slides
    resource: ../references/lecture-01.pdf
    title: Lecture 1 slides
---

# Lecture 1

The fitted line minimizes squared residuals.[^slides]

[^slides]: Lecture 1 slides, page 2.
```

Use ordinary Markdown links between pages. The path of a page is its OKF identity, so keep filenames stable. `index.md` and `log.md` have reserved roles in OKF; neither is a concept page.[^okf]

## Original files and student notes

Keep instructor PDFs, slides, readings, and rough exports in the course's `references/` folder. A student's working Markdown lecture note goes in `lectures/`. When importing an existing Markdown file without frontmatter, leave the original unchanged and add minimal `type` frontmatter only to the copy in the knowledge base. Keep the student's text and authorship. New agent-written content stays `draft` until the student reviews it.

`python3 check.py` performs a small local check for missing `type` frontmatter and broken Markdown links. It does not validate all of YAML or the full OKF specification.

[^okf]: Open Knowledge Format v0.2 specification, sections 3–5.
