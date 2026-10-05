from backend.ingestion.cleaner import clean_text


def test_cleaner():

    assert clean_text(
        "  hello   world "
    ) == "hello world"
