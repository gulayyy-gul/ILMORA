class ResearchService:

    def __init__(self, rag):

        self.rag = rag

    def research(
        self,
        query,
        **filters
    ):

        return self.rag.research(
            query,
            **filters
        )
