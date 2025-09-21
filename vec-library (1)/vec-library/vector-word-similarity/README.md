# Vector Word Similarity (VWS)

A lightweight, repo-ready scaffold to store and compute **word/phrase similarity** with VEC-aware metadata.
Designed for quick onboarding: drop your word-pair tables into `data/`, run one script, and get scored outputs in `data/results/`.

> This repo is tailored for Tony's VEC/ELS workflows (Conarion numbers, VEC tags like `1412`, `1942`, `1077`, etc.).
> Use the `vec_code_tags` column to associate semantic relations with specific VEC codes/sequences.

## Folder structure

```
vector-word-similarity/
├─ data/
│  ├─ word_pairs.csv                # Your master word/phrase pairs
│  ├─ vec_terms.csv                 # Optional: curated lexicon with VEC tags
│  └─ examples/                     # Mini samples to test the pipeline
├─ src/
│  ├─ compute_similarity.py         # CLI tool: read CSV, score, write results
│  └─ utils.py                      # Helpers (loading models, cleaning text)
├─ notebooks/
│  └─ 01_quickstart.ipynb           # Optional exploratory work
├─ .github/workflows/
│  └─ validate.yml                  # Lint/validate CSV on push
├─ .gitignore
├─ requirements.txt
├─ LICENSE
└─ README.md
```

## Quickstart

1. **Install**
   ```bash
   python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Add your data**
   - Put your master pairs in `data/word_pairs.csv`
   - (Optional) Put VEC lexicon entries in `data/vec_terms.csv`

3. **Run similarity**
   ```bash
   python src/compute_similarity.py      --pairs data/word_pairs.csv      --model all-MiniLM-L6-v2      --out data/results/word_pairs_scored.csv
   ```

4. **Read the results**
   - `similarity` ranges 0→1 (higher = more similar)
   - Use `relation_label` to keep your own ground-truth class (e.g., synonym/antonym/gate-link)

## CSV schemas

### `data/word_pairs.csv`
| column           | type   | description |
|------------------|--------|-------------|
| term_a           | str    | First word/phrase |
| term_b           | str    | Second word/phrase |
| relation_label   | str    | Your label (e.g., `synonym`, `antonym`, `ritual-link`, `gate`) |
| vec_code_tags    | str    | Comma-separated VEC codes (e.g., `1412,1942`) |
| notes            | str    | Optional free text |

### `data/vec_terms.csv` (optional)
| column        | type | description |
|---------------|------|-------------|
| term          | str  | Word/phrase |
| vec_code_tags | str  | Comma-separated VEC codes |
| family        | str  | e.g., `healing`, `abundance`, `protection` |
| notes         | str  | Optional free text |

## Model options

Uses [sentence-transformers](https://www.sbert.net/) models by default. Examples:
- `all-MiniLM-L6-v2` (fast, small, good baseline)
- `paraphrase-MiniLM-L12-v2`
- `multi-qa-MiniLM-L6-cos-v1`

You can also switch to spaCy or Gensim in `src/utils.py`.

## Safety for Public Repos
- No secrets, no API keys. This is fully local.
- Data lives in CSV. If anything is private, keep it out of the repo or publish a redacted version.

## License
MIT — see `LICENSE`.
