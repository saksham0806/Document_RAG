import os
import pickle
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_existing_chunks(path="data/processed/chunks.pkl"):
    """Load existing chunks if file exists."""
    if os.path.exists(path):
        with open(path, "rb") as f:
            return pickle.load(f)
    return []


def ingest_document(pdf_path, chunk_size=800, chunk_overlap=100):
    """
    Extracts text from a PDF, chunks it, and APPENDS them to the global chunks list.
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"File not found: {pdf_path}")

    print(f"\nProcessing: {pdf_path}")

    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    if not text.strip():
        raise ValueError("No text extracted. Is this a scanned PDF?")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    new_chunks = splitter.split_text(text)

    print(f"✔ Generated {len(new_chunks)} chunks from {pdf_path}")

    # ---- Load old chunks and append ----
    os.makedirs("data/processed", exist_ok=True)
    chunks_file = "data/processed/chunks.pkl"

    existing_chunks = load_existing_chunks(chunks_file)
    print(f"📦 Found {len(existing_chunks)} existing chunks, appending...")

    final_chunks = existing_chunks + new_chunks

    # ---- Save combined chunks ----
    with open(chunks_file, "wb") as f:
        pickle.dump(final_chunks, f)

    print(f"💾 Saved {len(final_chunks)} total chunks to {chunks_file}")

    return new_chunks


if __name__ == "__main__":
    folder = "data/documents"
    pdfs = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".pdf")]

    if not pdfs:
        print("No PDFs found in data/documents/")
    else:
        for pdf_path in pdfs:
            ingest_document(pdf_path)

        print("\nIngestion complete! Now run:")
