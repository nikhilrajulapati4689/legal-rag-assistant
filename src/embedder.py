from sentence_transformers import SentenceTransformer


MODEL_NAME = "all-MiniLM-L6-v2"


def create_embedding_model():
    return SentenceTransformer(MODEL_NAME)


if __name__ == "__main__":

    model = create_embedding_model()

    text = "A consumer has the right to seek compensation."

    embedding = model.encode(text)

    print("Embedding created successfully.")
    print("Vector dimensions:", len(embedding))
    print("First 10 values:")
    print(embedding[:10])