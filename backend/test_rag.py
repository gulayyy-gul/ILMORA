from backend.ingestion_service import IngestionService
from backend.rag_engine import ILMORARAG


PDF_PATH = "data/uploads/test.pdf"


def main():

    print("\nStarting ILMORA...\n")

    ingestion = IngestionService()

    print("Reading document...")

    documents = ingestion.ingest(
        PDF_PATH,
        metadata={
            "source_id": "test_source",
            "author": "Unknown",
            "book": "Test Book",
            "language": "Arabic",
            "category": "Tafsir",
        },
    )

    print(
        f"Created {len(documents)} chunks."
    )

    rag = ILMORARAG()

    print("Indexing documents...")

    count = rag.index_documents(
        documents
    )

    print(
        f"Indexed {count} chunks."
    )

    print("\nTesting research...\n")

    result = rag.research(
        "What is discussed in this source?"
    )

    print("\nANSWER:")
    print(
        result["answer"]
    )

    print("\nEVIDENCE:")

    for evidence in result["evidence"]:

        print(
            f"\n[{evidence['label']}]"
        )

        print(
            f"Book: {evidence['book']}"
        )

        print(
            f"Page: {evidence['page']}"
        )

        print(
            evidence["text"][:500]
        )


if __name__ == "__main__":
    main()
