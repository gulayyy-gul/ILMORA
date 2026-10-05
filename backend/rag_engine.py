from backend.retrieval.embeddings import load_embedding_model
from backend.retrieval.vector_store import get_collection
from backend.retrieval.keyword_search import KeywordIndex
from backend.retrieval.hybrid_search import reciprocal_rank_fusion
from backend.retrieval.reranker import rerank
from backend.llm.generator import generate_answer
from backend.citations.builder import build_evidence

from config.settings import (
    EMBEDDING_MODEL,
    CHROMA_DIR,
    TOP_K_VECTOR,
    TOP_K_KEYWORD,
    TOP_K_FINAL,
)


class ILMORARAG:

    def __init__(self):

        self.embedding_model = load_embedding_model(
            EMBEDDING_MODEL
        )

        self.collection = get_collection(
            path=CHROMA_DIR,
            name="ilmora"
        )

        self.documents = []

        self.keyword_index = None

        self._load_existing_documents()

    # ========================================================
    # LOAD EXISTING DOCUMENTS
    # ========================================================

    def _load_existing_documents(self):

        try:

            data = self.collection.get(
                include=["documents", "metadatas"]
            )

            documents = data.get(
                "documents",
                []
            )

            metadatas = data.get(
                "metadatas",
                []
            )

            ids = data.get(
                "ids",
                []
            )

            self.documents = []

            for index, text in enumerate(documents):

                metadata = {}

                if index < len(metadatas):
                    metadata = metadatas[index] or {}

                chunk_id = (
                    metadata.get("chunk_id")
                    or (
                        ids[index]
                        if index < len(ids)
                        else str(index)
                    )
                )

                document = {
                    "chunk_id": chunk_id,
                    "text": text,
                    **metadata,
                }

                self.documents.append(
                    document
                )

            if self.documents:

                self.keyword_index = KeywordIndex(
                    self.documents
                )

        except Exception:

            self.documents = []
            self.keyword_index = None

    # ========================================================
    # INDEX DOCUMENTS
    # ========================================================

    def index_documents(self, documents):

        if not documents:
            return 0

        texts = []
        ids = []
        metadatas = []

        for index, document in enumerate(documents):

            text = document.get(
                "text",
                ""
            ).strip()

            if not text:
                continue

            chunk_id = document.get(
                "chunk_id",
                f"chunk_{index}"
            )

            metadata = {
                key: value
                for key, value in document.items()
                if key not in ["text"]
            }

            texts.append(text)
            ids.append(chunk_id)
            metadatas.append(metadata)

        if not texts:
            return 0

        embeddings = self.embedding_model.encode(
            texts,
            normalize_embeddings=True
        )

        self.collection.upsert(
            ids=ids,
            documents=texts,
            embeddings=embeddings.tolist(),
            metadatas=metadatas,
        )

        self._load_existing_documents()

        return len(texts)

    # ========================================================
    # VECTOR SEARCH
    # ========================================================

    def _vector_search(
        self,
        query,
        k=12,
        filters=None,
    ):

        query_embedding = self.embedding_model.encode(
            [query],
            normalize_embeddings=True
        )

        where = None

        if filters:

            conditions = []

            for key, value in filters.items():

                if value and value != "All":

                    conditions.append(
                        {
                            key: value
                        }
                    )

            if len(conditions) == 1:

                where = conditions[0]

            elif len(conditions) > 1:

                where = {
                    "$and": conditions
                }

        kwargs = {
            "query_embeddings": query_embedding.tolist(),
            "n_results": k,
        }

        if where:
            kwargs["where"] = where

        result = self.collection.query(
            **kwargs
        )

        documents = []

        result_documents = (
            result.get("documents", [[]])[0]
        )

        result_metadatas = (
            result.get("metadatas", [[]])[0]
        )

        result_ids = (
            result.get("ids", [[]])[0]
        )

        for index, text in enumerate(
            result_documents
        ):

            metadata = {}

            if index < len(result_metadatas):
                metadata = (
                    result_metadatas[index]
                    or {}
                )

            chunk_id = (
                metadata.get("chunk_id")
                or (
                    result_ids[index]
                    if index < len(result_ids)
                    else str(index)
                )
            )

            documents.append(
                {
                    "chunk_id": chunk_id,
                    "text": text,
                    **metadata,
                }
            )

        return documents

    # ========================================================
    # RESEARCH
    # ========================================================

    def research(
        self,
        query,
        **filters
    ):

        if not query or not query.strip():

            return {
                "answer": (
                    "Please enter a research question."
                ),
                "evidence": [],
                "scholarly_views": [],
                "limitations": [
                    "No research question was provided."
                ],
                "evidence_labels_used": [],
            }

        if not self.documents:

            return {
                "answer": (
                    "I could not find sufficient evidence "
                    "in the indexed sources to answer this confidently."
                ),
                "evidence": [],
                "scholarly_views": [],
                "limitations": [
                    "No documents are currently indexed."
                ],
                "evidence_labels_used": [],
            }

        # ----------------------------------------------------
        # VECTOR SEARCH
        # ----------------------------------------------------

        vector_results = self._vector_search(
            query,
            k=TOP_K_VECTOR,
            filters=filters,
        )

        # ----------------------------------------------------
        # KEYWORD SEARCH
        # ----------------------------------------------------

        if self.keyword_index:

            keyword_results = self.keyword_index.search(
                query,
                k=TOP_K_KEYWORD
            )

        else:

            keyword_results = []

        # ----------------------------------------------------
        # HYBRID SEARCH
        # ----------------------------------------------------

        hybrid_results = reciprocal_rank_fusion(
            vector_results,
            keyword_results,
        )

        # ----------------------------------------------------
        # RERANK
        # ----------------------------------------------------

        final_documents = rerank(
            query,
            hybrid_results,
            top_k=TOP_K_FINAL,
        )

        # ----------------------------------------------------
        # BUILD EVIDENCE
        # ----------------------------------------------------

        evidence = []

        for index, document in enumerate(
            final_documents,
            start=1
        ):

            label = f"E{index}"

            evidence.append(
                build_evidence(
                    label,
                    document
                )
            )

        # ----------------------------------------------------
        # GENERATE ANSWER
        # ----------------------------------------------------

        generated = generate_answer(
            query,
            evidence
        )

        return {
            "answer": generated.get(
                "answer",
                ""
            ),
            "evidence": evidence,
            "scholarly_views": generated.get(
                "scholarly_views",
                []
            ),
            "limitations": generated.get(
                "limitations",
                []
            ),
            "evidence_labels_used": generated.get(
                "evidence_labels_used",
                []
            ),
        }

    # ========================================================
    # INDEXED CHUNKS
    # ========================================================

    def indexed_chunks(self):

        return self.documents

    # ========================================================
    # CLEAR VECTOR STORE
    # ========================================================

    def clear_vector_store(self):

        try:

            self.collection = get_collection(
                path=CHROMA_DIR,
                name="ilmora"
            )

            existing = self.collection.get()

            ids = existing.get(
                "ids",
                []
            )

            if ids:

                self.collection.delete(
                    ids=ids
                )

            self.documents = []
            self.keyword_index = None

        except Exception as error:

            raise RuntimeError(
                f"Could not clear vector store: {error}"
            )
