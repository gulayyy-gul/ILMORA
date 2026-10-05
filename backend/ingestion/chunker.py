def chunk_text(
    text,
    size=1200,
    overlap=180
):

    chunks = []

    start = 0

    while start < len(text):

        end = min(
            len(text),
            start + size
        )

        chunks.append(
            text[start:end]
        )

        if end == len(text):
            break

        start = max(
            0,
            end - overlap
        )

    return chunks
