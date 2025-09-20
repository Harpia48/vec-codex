# Publish to GitHub

## Option A — GitHub Desktop (easiest)
1. Open **GitHub Desktop** → *File* → *New repository from existing files...*.
2. Choose the extracted `vec-library` folder.
3. Commit and *Publish repository* (set to Private if you prefer).
4. Enable **Git LFS** in *Repository → Repository settings → Git LFS*.

## Option B — Command line
```bash
# install git lfs first:
git lfs install

# init and first commit
git init
git add .gitattributes .gitignore LICENSE README.md docs data site scripts
git commit -m "Init VEC Library structure"

# create a private repo on GitHub (web UI), then:
git branch -M main
git remote add origin https://github.com/<your-username>/vec-library.git
git push -u origin main
```
