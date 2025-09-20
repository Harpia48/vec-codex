# Repository Usage

## Adding a new VEC
1. Copy `TEMPLATE_VEC.md` from `data/vec_codes/`.
2. Rename to `####-name.md` (e.g., `1942-abundance-activator.md`).
3. Fill the front‑matter and sections. Commit.

## Adding a sigil
- Place PNG/SVG in `data/sigils/` (use Git LFS).
- Reference it inside the corresponding VEC entry with a relative path.

## Logging an ELS Daily Record
- Create `data/logs/els_daily/YYYY-MM-DD.md`.
- Use the template in that folder.

## FlowWheel Log
- Create `data/logs/flowwheel/YYYY-MM-DD.md` from template.

## Private Items
- You can mark sensitive files with `private: true` in front‑matter, or keep them in a separate private repo if needed.
