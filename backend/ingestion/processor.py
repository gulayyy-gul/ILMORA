from .cleaner import clean_text
from .chunker import chunk_text


def process_text(
    text,
    metadata=None
):

    metadata = metadata or {}

    cleaned = clean_text(text)

    chunks = chunk_text(cleaned)

    return [
        {
            "text": chunk,
            **metadata
        }
        for chunk in chunks
    ]
