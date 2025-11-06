from flask import Flask, request, jsonify
from ingest import ingest_document
from retriever import build_faiss_index
from query_engine import generate_answer
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    filepath = os.path.join("data/documents", file.filename)
    file.save(filepath)
    ingest_document(filepath)
    build_faiss_index()
    return jsonify({"status": "success", "message": "Document processed and indexed."})

@app.route('/query', methods=['POST'])
def query_doc():
    data = request.get_json()
    answer = generate_answer(data['query'])
    return jsonify({"answer": answer})

if __name__ == '__main__':
    os.makedirs("data/documents", exist_ok=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
