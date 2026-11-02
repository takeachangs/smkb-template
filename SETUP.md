---
type: Playbook
title: First-time SMKB setup
description: A guided conversation that builds a student's course knowledge base from existing materials.
tags: [okf, setup]
status: draft
generated: { by: Codex/gpt-6, at: 2026-11-02T02:55:52Z }
---

# First-time setup

Use this playbook when the user asks to set up this repository. Work with the student one step at a time; ask for missing information as it becomes relevant. If course folders already exist, inspect them and continue instead of starting over.

1. **Courses.** Ask for the term, time zone, and course names or codes. Create a course folder only for each course the student names.
2. **Existing material.** Ask where their syllabi, slides, assignments, and notes are. Inventory only files they point you to. Show a proposed destination for each file and let them correct it. Copy selected originals into `<COURSE>/references/`; never move or overwrite them. Existing student-written Markdown lecture notes belong in `<COURSE>/lectures/` and keep their authorship.
3. **Schedule.** Ask for their weekly timetable and use syllabi or announcements to find due dates. Write `schedule.md` with the time zone and a source for each date. Show conflicting dates instead of choosing silently. Leave unknown dates blank.
4. **Course pages.** Create `<COURSE>/course.md` from the available syllabus, with logistics, grading, and the course's AI policy where known. Create `lectures/`, `concepts/`, and `assignments/` as needed. Link new pages to their sources. Mark agent-written pages `status: draft`; never add a human-verification claim.
5. **Review.** Show the student the course list, upcoming dates, imported files, and unresolved questions. Check that Markdown links resolve and append a short entry to `log.md` describing what setup created.

Use OKF v0.2 for knowledge pages: YAML frontmatter with at least `type`, plus a useful `title`, one-sentence `description`, `status`, `generated` actor and UTC time, and source information when a page draws on a file. Keep the student's existing notes intact unless they ask you to edit them. Do not produce graded submission content when a course's AI policy disallows it.
