import argparse
import os
import pandas as pd
from utils import load_model, embed_texts, cosine_sim

def score_pairs(pairs_csv: str, out_csv: str, model_name: str):
    df = pd.read_csv(pairs_csv)
    # Basic sanity
    for col in ["term_a", "term_b"]:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")
    model = load_model(model_name)
    a_vecs = embed_texts(model, df["term_a"].astype(str).tolist())
    b_vecs = embed_texts(model, df["term_b"].astype(str).tolist())

    sims = [float((a_vecs[i] * b_vecs[i]).sum()) for i in range(len(df))]
    out = df.copy()
    out["similarity"] = sims
    os.makedirs(os.path.dirname(out_csv), exist_ok=True)
    out.to_csv(out_csv, index=False)
    print(f"Wrote {out_csv} with {len(out)} rows.")

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Compute word/phrase pair similarity")
    ap.add_argument("--pairs", required=True, help="CSV path with term_a,term_b,...")
    ap.add_argument("--out", required=True, help="Output CSV (e.g., data/results/word_pairs_scored.csv)")
    ap.add_argument("--model", dest="model", default="all-MiniLM-L6-v2", help="SentenceTransformer model name")
    args = ap.parse_args()
    score_pairs(args.pairs, args.out, args.model)
