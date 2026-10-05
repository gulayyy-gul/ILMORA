import fitz


def extract_pdf(path):

    document = fitz.open(path)

    pages = []

    for number, page in enumerate(
        document,
        start=1
    ):

        pages.append(
            {
                "page": number,
                "text": page.get_text("text")
            }
        )

    return pages
