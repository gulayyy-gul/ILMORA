def rerank(
    query,
    documents,
    top_k=6
):

    query_tokens = set(
        query.lower().split()
    )

    scored = []

    for document in documents:

        document_tokens = set(
            document
            .get("text", "")
            .lower()
            .split()
        )

        overlap = len(
            query_tokens
            & document_tokens
        )

        score = (
            overlap
            + document.get(
                "hybrid_score",
                0
            )
        )

        scored.append(
            (
                score,
                document
            )
        )

    scored.sort(
        key=lambda item: item[0],
        reverse=True
    )

    return [
        document
        for score, document
        in scored[:top_k]
    ]
