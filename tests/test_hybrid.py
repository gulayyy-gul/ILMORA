from backend.retrieval.hybrid_search import reciprocal_rank_fusion


def test_rff():

    result = reciprocal_rank_fusion(
        [
            {
                "chunk_id": "a",
                "text": "one"
            }
        ],
        [
            {
                "chunk_id": "b",
                "text": "two"
            }
        ]
    )

    assert len(result) == 2
