class ILMORARAG:

    def index_documents(self, documents):
        raise NotImplementedError(
            "Connect ingestion and retrieval modules here."
        )

    def research(self, query, **filters):
        raise NotImplementedError(
            "Connect hybrid retrieval and LLM generation here."
        )

    def indexed_chunks(self):
        return []

    def clear_vector_store(self):
        pass
