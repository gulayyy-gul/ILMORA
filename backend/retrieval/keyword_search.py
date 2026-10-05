from rank_bm25 import BM25Okapi


class KeywordIndex:

    def __init__(self, documents):

        self.documents = documents

        tokenized_documents = [
            document["text"].split()
            for document in documents
        ]

        self.model = BM25Okapi(
            tokenized_documents
        )

    def search(
        self,
        query,
        k=12
    ):

        scores = self.model.get_scores(
            query.split()
        )

        ranked = sorted(
            zip(
                self.documents,
                scores
            ),
            key=lambda item: item[1],
            reverse=True
        )

        return [
            document
            for document, score
            in ranked[:k]
        ]
