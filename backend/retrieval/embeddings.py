from sentence_transformers import SentenceTransformer


def load_embedding_model(name):

    return SentenceTransformer(name)
