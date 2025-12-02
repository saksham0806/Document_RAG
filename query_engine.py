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

def generate_answer(query, k=5):
    retrieved_chunks = retrieve_context(query, k=k)

    if not retrieved_chunks:
        return "No relevant context found. Please ensure the document is indexed."

    context_text = "\n\n".join(retrieved_chunks)
    prompt = f"""
Context: {context_text}
Question: {query}
Answer:"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system","content": """ You are an AI assistant with access to document context. 
             Use only the provided context to answer the question factually. Answer based on given context only"""},
            {"role": "user", "content": prompt}],
        temperature=0.4
    )

    return response.choices[0].message.content.strip()