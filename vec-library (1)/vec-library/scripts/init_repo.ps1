Write-Host "Initializing VEC Library git repo..."
git init

# Git LFS note
try {
  git lfs install
} catch {
  Write-Host "NOTE: Install Git LFS from https://git-lfs.github.com/ if you plan to track large images."
}

git add .
git commit -m "Init VEC Library structure"
git branch -M main

Write-Host ""
Write-Host "Create a new (private) repo on GitHub, then run:"
Write-Host "  git remote add origin https://github.com/<your-username>/vec-library.git"
Write-Host "  git push -u origin main"
