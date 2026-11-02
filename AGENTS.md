---
type: Instructions
title: SMKB agent instructions
description: Routes first-time setup, ingestion, and project-level skill creation.
tags: [okf, agent-instructions]
status: draft
generated: { by: Codex/gpt-6, at: 2026-11-02T02:55:52Z }
---

# Agent instructions

When the user asks to set up this repository for the first time, read `SETUP.md` and follow its onboarding workflow.

When the user asks to ingest a course file or today's work, use `.agents/skills/ingest/SKILL.md`.

When the user asks to create or update a skill, put it in this repository under `.agents/skills/<name>/SKILL.md` and add a project-level Claude entry under `.claude/skills/<name>/SKILL.md`. Do not put project skills in a user-level directory.

For knowledge documents, use OKF v0.2: Markdown with YAML frontmatter and a `type`. Include a title, one-sentence description, `generated` actor and time, sources for source-derived facts, and standard Markdown links. New agent-written pages start with `status: draft`; only the student adds human verification. Preserve original course files, flag conflicting facts, and follow each course's AI policy.
