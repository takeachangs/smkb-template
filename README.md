---
type: Guide
title: SMKB Template
description: Workshop starter for a personal course knowledge base maintained with an AI agent.
tags: [okf, workshop, template]
status: draft
generated: { by: Codex/gpt-6, at: 2026-11-02T02:55:52Z }
---

# SMKB Template

Materials for the [UofT AI workshop: Create an AI agent to manage your courses](https://luma.com/ckdrzi3m).

This repository helps you build a personal course knowledge base from the notes and files you already have. Your AI agent asks about your courses and timetable, organizes the files you choose, and writes pages using Open Knowledge Format (OKF). You check the dates and any notes it creates.

## What's in here

```text
smkb-template/
├── README.md                         # you are here
├── AGENTS.md                         # routes setup, ingestion, and skill requests
├── CLAUDE.md                         # points Claude to AGENTS.md
├── SETUP.md                          # first-time setup conversation
├── .gitignore                         # local files and secrets to exclude from Git
├── .agents/skills/ingest/SKILL.md    # project-level ingestion workflow
└── .claude/skills/ingest/SKILL.md    # Claude entry for that workflow
```

Setup creates your course folders, `schedule.md`, and `log.md` with you. The repository starts without your personal course files.

## The two workflows

### Set up your knowledge base

Open this folder in an AI agent that can read and write local files. Say:

> Set up this knowledge base for me.

The agent follows `SETUP.md`. It asks about your courses, existing materials, and timetable one step at a time. It shows you where it plans to put files before copying them into the knowledge base.

### Ingest new material

When you get new slides, a syllabus, an assignment, or lecture notes, point the agent to the file and say:

> Ingest this file into my course: [file path].

The project-level ingest skill preserves the original, updates the relevant course pages, and reports anything you need to check.

## How to start

- **With Git:** use **Use this template** on GitHub, choose a private repository for your course notes, then clone your copy.
- **Without Git:** use **Code → Download ZIP**, unzip it, and open the folder in your AI agent.

Bring your own course files. Git is optional. The local setup works before you connect Canvas or other services.
