# IntelliDoc - Intelligent Document Query System

A smart document processing system that lets you chat with your PDFs using AI. Built with Python, Flask, and OpenAI's GPT.

## Features

- PDF document processing and text extraction
- Semantic search using FAISS indexing
- AI-powered question answering using GPT
- Simple web API interface
- Fast and efficient document chunking

## Tech Stack

- **Backend**: Python, Flask
- **AI/ML**: OpenAI GPT, Sentence Transformers
- **Vector Database**: FAISS
- **Document Processing**: PyPDF2, LangChain
- **Containerization**: Docker

## Getting Started

### Prerequisites

- Python 3.10 or higher
- pip package manager
- OpenAI API key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/IntelliDoc.git
cd IntelliDoc
```

2. Create and activate a virtual environment:
```bash
python -m venv ragenv
source ragenv/bin/activate  # On Windows: ragenv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Place your PDF documents in the `data/documents` folder

2. Run the Flask application:
```bash
python app.py
```

3. Upload a document:
```bash
curl -X POST -F "file=@your_document.pdf" http://localhost:5000/upload
```

4. Query your document:
```bash
curl -X POST -H "Content-Type: application/json" \
     -d '{"query":"your question here"}' \
     http://localhost:5000/query
```

## Docker Support

Build and run using Docker:

```bash
docker build -t intellidoc .
docker run -p 5000:5000 intellidoc
```


## Contributing

Feel free to fork this project and submit pull requests. You can also open issues for bugs or feature requests.

## License

This project is open source and available for anyone trying to complete thier project :)