import os, sys, glob, yaml

ROOT = os.path.dirname(os.path.dirname(__file__))
vec_dir = os.path.join(ROOT, "data", "vec_codes")

errors = 0
for f in glob.glob(os.path.join(vec_dir, "*.md")):
    txt = open(f, "r", encoding="utf-8").read()
    if not txt.strip().startswith("---"):
        print(f"[WARN] {os.path.basename(f)}: missing front-matter")
        errors += 1
print("Validation complete.")
sys.exit(0 if errors == 0 else 1)
