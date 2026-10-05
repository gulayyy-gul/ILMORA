def reciprocal_rank_fusion(
    vector_results,
    keyword_results,
    k=60
):

    scores = {}

    documents = {}

    for rank, document in enumerate(
        vector_results,
        start=1
    ):

        key = document.get(
            "chunk_id",
            str(document)
        )

        documents[key] = document

        scores[key] = (
            scores.get(key, 0)
            + 1 / (k + rank)
        )

    for rank, document in enumerate(
        keyword_results,
        start=1
    ):

        key = document.get(
            "chunk_id",
            str(document)
        )

        documents[key] = document

        scores[key] = (
            scores.get(key, 0)
            + 1 / (k + rank)
        )

    result = [
        {
            **documents[key],
            "hybrid_score": scores[key]
        }
        for key in scores
    ]

    return sorted(
        result,
        key=lambda item: item["hybrid_score"],
        reverse=True
    )
