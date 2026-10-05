from backend.ingestion.chunker import chunk_text


def test_chunker():

    chunks = chunk_text(
        "a" * 2500
    )

    assert len(chunks) > 1
