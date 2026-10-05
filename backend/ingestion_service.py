class IngestionService:

    def ingest(
        self,
        source_path,
        metadata=None
    ):
        return {
            "source_path": source_path,
            "metadata": metadata or {}
        }
