---
name: ingest
description: Integrate a user-identified course file into an existing SMKB knowledge base when the user asks to ingest it.
---

# Ingest course material

Use this workflow for a named syllabus, lecture file, assignment, announcement, or student note. Ask which course it belongs to only when the path or context does not make that clear.

1. Check whether the source has already been ingested so the same file does not create duplicate pages.
2. Preserve the original. Copy new PDFs, slides, handouts, or rough exports into `<COURSE>/references/` if the user wants them in the repository; never move or overwrite a source. Keep a student's working Markdown lecture note in `<COURSE>/lectures/`.
3. Add only what the source supports: a syllabus updates `course.md`; lecture material updates a lecture note and short linked concept notes; an assignment gets a summary, due date, and links to relevant material without solving graded questions. Preserve student-authored text unless the user asks for editing.
4. Record source paths and page or section references for specific facts, plus the generating actor and UTC time. Mark new agent-written notes `status: draft`; do not add `verified`. If a date appears, update `schedule.md` with its source and flag any disagreement.
5. Check links, append a short entry to `log.md`, and tell the user which files changed and what still needs review.
