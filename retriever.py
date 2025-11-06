import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import os, pickle

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def build_faiss_index(processed_dir="data/processed/", index_dir="data/faiss_index/"):
    os.makedirs(index_dir, exist_ok=True)
    texts = []
    for file in os.listdir(processed_dir):
        with open(os.path.join(processed_dir, file), 'r') as f:
            texts += f.read().split("\n---\n")

    embeddings = model.encode(texts, show_progress_bar=True)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))
    faiss.write_index(index, os.path.join(index_dir, "index.faiss"))
    pickle.dump(texts, open(os.path.join(index_dir, "texts.pkl"), "wb"))
    print(f"FAISS index built with {len(texts)} documents.")
