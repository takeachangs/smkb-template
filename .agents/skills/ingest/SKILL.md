---
name: ingest
description: Integrate a course file or recent study conversation into SMKB when the user asks to ingest material or today's work.
---

# Ingest course material

Use this workflow for a named file or work from the current conversation. Infer the course, topic, and source from context; ask only when something needed to write the note is unclear. For "today's work," use what actually happened in this conversation rather than inventing a file or lecture.

1. Check whether the file or conversation work has already been ingested so it does not create duplicate pages.
2. For files, preserve the original. Copy new PDFs, slides, handouts, or rough exports into `<COURSE>/references/` if the user wants them in the repository; never move or overwrite a source. Keep a student's working Markdown lecture note in `<COURSE>/lectures/`.
3. Add only what the source supports: a syllabus updates `course.md`; lecture material updates a lecture note and short linked concept notes; an assignment gets a summary, due date, and links to relevant material without solving graded questions. For today's work, update the relevant course notes or create a dated draft study note in the course folder. Preserve student-authored text unless the user asks for editing.
4. Attribute facts to the file and page or section where possible. For conversation work, identify the session and date as the source, without presenting it as instructor material. Record the generating actor and UTC time. Mark new agent-written notes `status: draft`; do not add `verified`. If a date appears, update `schedule.md` with its source and flag any disagreement.
5. Check links, append a short entry to `log.md`, and tell the user which files changed and what still needs review.
