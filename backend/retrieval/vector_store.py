import chromadb


def get_client(
    path="data/chroma"
):

    return chromadb.PersistentClient(
        path=path
    )


def get_collection(
    path="data/chroma",
    name="ilmora"
):

    client = get_client(path)

    return client.get_or_create_collection(
        name=name
    )
