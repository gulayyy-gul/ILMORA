from backend.citations.builder import build_evidence


def test_citation():

    result = build_evidence(
        "E1",
        {
            "chunk_id": "X",
            "text": "sample"
        }
    )

    assert result["label"] == "E1"
