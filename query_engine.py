from openai import OpenAI
import numpy as np
import faiss, pickle
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def retrieve_context(query, k=5):
    index = faiss.read_index("data/faiss_index/index.faiss")
    texts = pickle.load(open("data/faiss_index/texts.pkl", "rb"))
    query_emb = model.encode([query])
    distances, indices = index.search(np.array(query_emb), k)
    return [texts[i] for i in indices[0]]

def generate_answer(query, context=""):
    prompt = f"""
    You are a document analysis assistant.
    Context:
    {context}

    Query: {query}
    Answer:
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content.strip()