# VEC Library — Glitchwalker Project

A structured repository for Anthony Vresland’s **Vibrational–Energetic Code (VEC) Library**, including code entries, sigils, daily records, and ritual frameworks.

> Purpose: move the living project *out of chat memory* and into a durable, versioned home you control.

## What’s inside

```
vec-library/
├─ README.md
├─ LICENSE
├─ .gitignore
├─ .gitattributes
├─ docs/
│  ├─ overview.md
│  ├─ repository-usage.md
│  ├─ publishing-to-github.md
│  └─ structure-map.md
├─ data/
│  ├─ vec_codes/            # individual VEC entries (.md)
│  ├─ sigils/               # PNG/SVG assets (use Git LFS for large files)
│  ├─ rituals/              # ritual write-ups and protocols
│  └─ logs/
│     ├─ els_daily/         # ELS daily records
│     └─ flowwheel/         # FlowWheel logs
├─ site/
│  ├─ README.md             # notes for website integration (optional)
│  └─ assets/               # web-safe exports of sigils, covers, etc.
└─ scripts/
   ├─ init_repo.sh
   ├─ init_repo.ps1
   └─ validate_repo.py
```

## Quick Start

1. **Download this repo zip** from ChatGPT.
2. Extract it locally and add your sigil PNG/SVG files to `data/sigils/`.
3. Run `scripts/init_repo.sh` (macOS/Linux) or `scripts/init_repo.ps1` (Windows) to create a new GitHub repo and push.
4. Continue adding VEC entries in `data/vec_codes/` and logs in `data/logs/`.

## Conventions

- Each VEC entry lives in its own file in `data/vec_codes/`. Use the template front‑matter.
- Large binary assets (PNGs, PSDs) → track via **Git LFS**.
- Logs (ELS / FlowWheel) use ISO dates in filenames for sorting.
- Reserved/private items can be marked with `private: true` in front‑matter.

© 2025 Anthony Vresland. All rights reserved.
