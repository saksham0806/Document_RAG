import re

def clean_text(text: str) -> str:
    """
    Clean text by removing extra spaces, newlines, and special characters.
    Keeps the text readable and ready for embedding.
    """
    text = text.replace('\n', ' ')
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)  # Remove non-ASCII chars
    return text.strip()
