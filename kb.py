#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""lint / index / viz for this OKF bundle. Self-contained: helpers are vendored in .kb/.

    ./kb.py lint     validate frontmatter, report broken links, list draft / unverified / stale docs
    ./kb.py index    regenerate every index.md
    ./kb.py viz      write viz.html

Runs via uv (the shebang). Without uv: python3 -m venv .venv && .venv/bin/pip install pyyaml && .venv/bin/python kb.py ...
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / ".kb"))

from document import OKFDocument, OKFDocumentError, is_stale, trust_tier  # noqa: E402
from viewer.generator import generate_visualization  # noqa: E402

LINK_RE = re.compile(r"\]\(([^)\s]+\.md)(?:#[^)]*)?\)")
OKF_VERSION = '---\nokf_version: "0.2"\n---\n\n'


def concepts():
    """Every concept document: *.md outside dot-directories, excluding index.md and nested git repos."""
    for p in sorted(ROOT.rglob("*.md")):
        rel = p.relative_to(ROOT)
        if (
            p.name != "index.md"
            and not any(part.startswith(".") for part in rel.parts)
            and not any((parent / ".git").exists() for parent in p.parents if parent != ROOT)
        ):
            yield p


def load(p):
    doc = OKFDocument.parse(p.read_text(encoding="utf-8"))
    doc.validate()
    return doc


def lint():
    problems = 0
    flagged = []
    for p in concepts():
        rel = p.relative_to(ROOT)
        try:
            doc = load(p)
        except (OKFDocumentError, ValueError) as e:
            print(f"ERROR   {rel}: {e}")
            problems += 1
            continue
        for target in LINK_RE.findall(doc.body):
            if target.startswith(("http://", "https://")):
                continue
            path = ROOT / target.lstrip("/") if target.startswith("/") else p.parent / target
            if not path.exists():
                print(f"MISSING {rel} -> {target}")
                problems += 1
        fm = doc.frontmatter
        flags = [f for f, on in (
            ("draft", fm.get("status") == "draft"),
            ("unverified", trust_tier(fm) == "unverified"),
            ("STALE", is_stale(fm)),
        ) if on]
        if flags:
            flagged.append((str(rel), ", ".join(flags)))
    if flagged:
        width = max(len(r) for r, _ in flagged)
        print("\nNeeds attention:")
        for rel, flags in flagged:
            print(f"  {rel:<{width}}  {flags}")
    print(f"\n{problems} problem(s)")
    return 1 if problems else 0


def index():
    """One index.md per directory that (transitively) holds concepts, deepest first so parents can cite children."""
    dirs = {ROOT}
    for p in concepts():
        d = p.parent
        while d != ROOT:
            dirs.add(d)
            d = d.parent
    blurbs = {}
    for d in sorted(dirs, key=lambda d: -len(d.parts)):
        by_type, subdirs = defaultdict(list), []
        for child in sorted(d.iterdir()):
            if child in dirs:
                subdirs.append(child)
            elif child.suffix == ".md" and child.name != "index.md" and not child.name.startswith("."):
                try:
                    fm = load(child).frontmatter
                except (OKFDocumentError, ValueError):
                    continue
                by_type[str(fm.get("type") or "Other")].append(
                    (str(fm.get("title") or child.stem), child.name, str(fm.get("description") or "")))
        lines = []
        for typ in sorted(by_type):
            lines.append(f"# {typ}\n")
            for title, link, desc in sorted(by_type[typ], key=lambda e: e[0].lower()):
                lines.append(f"* [{title}]({link})" + (f" - {desc}" if desc else ""))
            lines.append("")
        if subdirs:
            lines.append("# Subdirectories\n")
            for s in subdirs:
                lines.append(f"* [{s.name}]({s.name}/index.md)" + (f" - {blurbs[s]}" if blurbs.get(s) else ""))
            lines.append("")
        # A directory's blurb is its Course doc's description when it has one, else a count.
        course = by_type.get("Course")
        n = sum(len(v) for v in by_type.values()) + len(subdirs)
        blurbs[d] = course[0][2] if course else f"Contains {n} {'entry' if n == 1 else 'entries'}."
        text = "\n".join(lines)
        (d / "index.md").write_text((OKF_VERSION if d == ROOT else "") + text, encoding="utf-8")
    print(f"wrote {len(dirs)} index.md files")
    return 0


def viz():
    counts = generate_visualization(ROOT, ROOT / "viz.html", bundle_name="SMKB")
    print(f"viz.html: {counts['concepts']} concepts, {counts['edges']} edges")
    return 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    sys.exit({"lint": lint, "index": index, "viz": viz}.get(cmd, lambda: (print(__doc__), 2))())
