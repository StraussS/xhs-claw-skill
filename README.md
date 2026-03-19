# xhs-claw-skill

A production-ready OpenClaw skill project for Xiaohongshu (小红书) automation.

It provides local browser-driven workflows for:
- login and account management
- search, feed detail, and comment retrieval
- like and favorite actions
- image post publishing
- video publishing
- long-article publishing

## Project layout

- `SKILL.md` — skill entrypoint and routing guidance
- `references/` — operational docs, risk notes, acceptance report
- `scripts/` — Python automation scripts and helpers
- `tests/` — lightweight tests

## Requirements

- Python 3.11+
- Chrome or Chromium
- `uv` recommended for dependency setup

## Quick start

```bash
uv sync
python scripts/doctor.py
python scripts/cli.py check-login
```

## Core helper scripts

```bash
python scripts/doctor.py
python scripts/publish_preflight.py --title-file /tmp/title.txt --content-file /tmp/content.txt --images /abs/path/pic.jpg
python scripts/prod_smoke.py
```

## Validated capabilities

See:
- `references/risk-checklist.md`
- `references/production-hardening.md`

## Notes

This project is designed as a local OpenClaw-native skill project, not an MCP-based integration.
