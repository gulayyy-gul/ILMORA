def build_evidence(
    label,
    chunk
):

    return {
        "label": label,
        "chunk_id": chunk.get(
            "chunk_id"
        ),
        "author": chunk.get(
            "author"
        ),
        "book": chunk.get(
            "book"
        ),
        "volume": chunk.get(
            "volume"
        ),
        "page": chunk.get(
            "page"
        ),
        "text": chunk.get(
            "text",
            ""
        )
    }
