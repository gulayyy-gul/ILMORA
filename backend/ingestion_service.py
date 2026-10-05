import os

from backend.ingestion.pdf_loader import extract_pdf
from backend.ingestion.cleaner import clean_text
from backend.ingestion.chunker import chunk_text


class IngestionService:

    def ingest(
        self,
        source_path,
        metadata=None
    ):

        if not source_path:
            raise ValueError(
                "A source file is required."
            )

        if not os.path.exists(source_path):
            raise FileNotFoundError(
                f"Source file not found: {source_path}"
            )

        metadata = metadata or {}

        extension = os.path.splitext(
            source_path
        )[1].lower()

        if extension == ".pdf":

            pages = extract_pdf(
                source_path
            )

        elif extension == ".txt":

            with open(
                source_path,
                "r",
                encoding="utf-8",
                errors="ignore"
            ) as file:

                text = file.read()

            pages = [
                {
                    "page": 1,
                    "text": text
                }
            ]

        else:

            raise ValueError(
                "Unsupported file type. "
                "Only PDF and TXT files are supported."
            )

        documents = []

        for page_data in pages:

            page_number = page_data.get(
                "page",
                1
            )

            raw_text = page_data.get(
                "text",
                ""
            )

            cleaned = clean_text(
                raw_text
            )

            if not cleaned:
                continue

            chunks = chunk_text(
                cleaned
            )

            for chunk_number, chunk in enumerate(
                chunks,
                start=1
            ):

                chunk_id = (
                    f"{metadata.get('source_id', 'source')}"
                    f"_P{page_number}"
                    f"_C{chunk_number}"
                )

                document = {
                    "chunk_id": chunk_id,
                    "text": chunk,
                    "page": page_number,
                    "chunk_number": chunk_number,
                    "source_path": source_path,
                    "author": metadata.get(
                        "author",
                        "Unknown"
                    ),
                    "book": metadata.get(
                        "book",
                        os.path.basename(source_path)
                    ),
                    "volume": metadata.get(
                        "volume",
                        ""
                    ),
                    "chapter": metadata.get(
                        "chapter",
                        ""
                    ),
                    "language": metadata.get(
                        "language",
                        "Unknown"
                    ),
                    "category": metadata.get(
                        "category",
                        "Unknown"
                    ),
                    "source_id": metadata.get(
                        "source_id",
                        "source"
                    ),
                }

                documents.append(
                    document
                )

        return documents
