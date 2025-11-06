import os
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from utils import clean_text

def ingest_document(filepath, output_dir="data/processed/"):
    reader = PdfReader(filepath)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    text = clean_text(text)
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(text)
    
    os.makedirs(output_dir, exist_ok=True)
    filename = os.path.basename(filepath).replace('.pdf', '_chunks.txt')
    with open(os.path.join(output_dir, filename), 'w') as f:
        f.write("\n---\n".join(chunks))
    
    print(f"Document {filepath} processed into {len(chunks)} chunks.")
