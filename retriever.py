import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def retrieve_context(query, k=5):
    index = faiss.read_index("data/faiss_index/index.faiss")
    texts = pickle.load(open("data/faiss_index/texts.pkl", "rb"))

    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), k)
    
    results = []
    for idx in indices[0]:
        if idx < len(texts):
            results.append({"text": texts[idx]})
    return results

model = SentenceTransformer('all-MiniLM-L6-v2')

def build_faiss_index(
    chunks_folder="data/processed/chunks.pkl",
    index_folder="data/faiss_index"
):
    """
    Builds a FAISS index from processed text chunks.
    """
    os.makedirs(index_folder, exist_ok=True)

    if not os.path.exists(chunks_folder):
        raise FileNotFoundError(
            f"No chunks found at {chunks_folder}. Please run ingest.py first."
        )

    with open(chunks_folder, "rb") as f:
        texts = pickle.load(f)

    if not texts:
        raise ValueError("No text chunks to index. Check preprocessing pipeline.")

    print("🔹 Generating embeddings for", len(texts), "chunks...")
    embeddings = model.encode(texts, show_progress_bar=True)
    embeddings = np.array(embeddings).astype("float32")

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    faiss.write_index(index, os.path.join(index_folder, "index.faiss"))
    with open(os.path.join(index_folder, "texts.pkl"), "wb") as f:
        pickle.dump(texts, f)

    print(f"FAISS index built and saved to {index_folder}/")

