#!/usr/bin/env python3
"""Check the basic OKF shape and local Markdown links in this repository."""

from pathlib import Path
import re
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parent
TYPE_LINE = re.compile(r"^type:[ \t]*[^#\s]", re.MULTILINE)
LINK = re.compile(r"\]\(([^)]+)\)")


def documents():
    for path in sorted(ROOT.rglob("*.md")):
        relative = path.relative_to(ROOT)
        if any(part.startswith(".") for part in relative.parts):
            continue
        if path.name in {"index.md", "log.md"}:
            continue
        yield path, relative


def target_path(raw, parent):
    raw = raw.strip()
    if raw.startswith("<"):
        target = raw[1:].split(">", 1)[0]
    else:
        target = raw.split(None, 1)[0]
    target = unquote(target.split("#", 1)[0])
    if not target.endswith(".md") or "://" in target or target.startswith("mailto:"):
        return None
    return ROOT / target.lstrip("/") if target.startswith("/") else parent / target


def main():
    problems = []
    for path, relative in documents():
        lines = path.read_text(encoding="utf-8").splitlines()
        if not lines or lines[0] != "---":
            problems.append(f"{relative}: missing YAML frontmatter")
            continue
        try:
            end = lines.index("---", 1)
        except ValueError:
            problems.append(f"{relative}: unclosed YAML frontmatter")
            continue
        if not TYPE_LINE.search("\n".join(lines[1:end])):
            problems.append(f"{relative}: missing type")
        body = "\n".join(lines[end + 1 :])
        for raw in LINK.findall(body):
            target = target_path(raw, path.parent)
            if target is not None and not target.is_file():
                problems.append(f"{relative}: missing link target {raw}")
    for problem in problems:
        print(problem)
    print(f"{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
