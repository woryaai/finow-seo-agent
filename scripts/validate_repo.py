#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

COMMANDS = [
    "finow-keyword-research",
    "finow-build-website",
    "finow-blog-post",
    "finow-service-page",
    "finow-seo-optimization",
    "finow-publish",
    "finow-audit",
]

REQUIRED = [
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    "context/setup.md",
    "context/finow-brand.md",
    "context/finow-audiences.md",
    "context/finow-voice.md",
    "context/finow-compliance.md",
    "context/finow-product-facts.md",
    "context/competitors.md",
    "references/iran-search.md",
    "references/on-page-seo.md",
    "references/technical-seo.md",
    "references/geo-ai.md",
    "references/internal-linking.md",
    "references/schema.md",
    "references/content-quality.md",
    "references/programmatic-seo.md",
    "references/persian-writing.md",
    "references/audit-scoring.md",
    "keyword-map.md",
    "website-index.md",
    "optimization-log.md",
    "audit-report.md",
]

errors = []

for rel in REQUIRED:
    p = ROOT / rel
    if not p.exists():
        errors.append(f"missing required file: {rel}")
    elif p.is_file() and p.stat().st_size == 0:
        errors.append(f"required file is empty: {rel}")

for name in COMMANDS:
    canonical = ROOT / "commands" / f"{name}.md"
    wrapper = ROOT / ".claude" / "commands" / f"{name}.md"
    if not canonical.exists():
        errors.append(f"missing canonical command: {canonical.relative_to(ROOT)}")
    if not wrapper.exists():
        errors.append(f"missing Claude wrapper: {wrapper.relative_to(ROOT)}")
    else:
        text = wrapper.read_text(encoding="utf-8")
        expected = f"commands/{name}.md"
        if expected not in text:
            errors.append(f"Claude wrapper does not dispatch to {expected}")

agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8") if (ROOT / "AGENTS.md").exists() else ""
for name in COMMANDS:
    if f"/{name}" not in agents:
        errors.append(f"AGENTS.md dispatcher missing /{name}")

facts = (ROOT / "context/finow-product-facts.md").read_text(encoding="utf-8") if (ROOT / "context/finow-product-facts.md").exists() else ""
if "REVERIFY" not in facts:
    errors.append("product facts file must preserve explicit REVERIFY gate for volatile seed claims")

if errors:
    print("Finow SEO Agent validation: FAILED")
    for e in errors:
        print(f"- {e}")
    sys.exit(1)

print("Finow SEO Agent validation: PASS")
print(f"- {len(COMMANDS)} canonical commands")
print(f"- {len(COMMANDS)} Claude Code slash-command wrappers")
print(f"- {len(REQUIRED)} required context/reference/registry files")
