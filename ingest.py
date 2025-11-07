import os
import pickle
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def ingest_document(pdf_path, chunk_size=800, chunk_overlap=100):
    """
    Extracts text from a PDF, chunks it, and saves for indexing.
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"File not found: {pdf_path}")

    print(f"Processing: {pdf_path}")

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
    chunks = splitter.split_text(text)

    print(f"Generated {len(chunks)} chunks from {pdf_path}")

    os.makedirs("data/processed", exist_ok=True)
    with open("data/processed/chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

    print("Saved chunks to data/processed/chunks.pkl")
    return chunks


if __name__ == "__main__":
    folder = "data/documents"
    pdfs = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".pdf")]
    if not pdfs:
        print("No PDFs found in data/documents/")
    else:
        for pdf_path in pdfs:
            ingest_document(pdf_path)
