import os
from typing import List, Tuple
import numpy as np

try:
    from sentence_transformers import SentenceTransformer
except Exception:
    SentenceTransformer = None

DEFAULT_MODEL = "all-MiniLM-L6-v2"

def load_model(model_name: str = None):
    model_name = model_name or DEFAULT_MODEL
    if SentenceTransformer is None:
        raise RuntimeError("sentence-transformers not installed. Try: pip install sentence-transformers")
    return SentenceTransformer(model_name)

def embed_texts(model, texts: List[str]) -> np.ndarray:
    return np.asarray(model.encode(texts, normalize_embeddings=True))

def cosine_sim(a: np.ndarray, b: np.ndarray) -> float:
    # a, b are 1D vectors
    return float(np.dot(a, b))
