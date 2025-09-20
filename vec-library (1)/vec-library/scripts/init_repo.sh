#!/usr/bin/env bash
set -euo pipefail

echo "Initializing VEC Library git repo..."
git init

# Ensure Git LFS is set up (safe if already installed)
if command -v git-lfs >/dev/null 2>&1; then
  git lfs install
else
  echo "NOTE: git-lfs not found. Install from https://git-lfs.github.com/ if you will store large images."
fi

git add .
git commit -m "Init VEC Library structure"
git branch -M main

echo
echo "Now create a new (private) repo on GitHub, then run:"
echo "  git remote add origin https://github.com/<your-username>/vec-library.git"
echo "  git push -u origin main"
