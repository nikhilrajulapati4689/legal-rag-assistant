import pickle

import faiss
from sentence_transformers import SentenceTransformer


INDEX_PATH = "vectorstore/legal.index"
METADATA_PATH = "vectorstore/metadata.pkl"

MODEL_NAME = "all-MiniLM-L6-v2"

TOP_K = 3


def load_resources():

    index = faiss.read_index(INDEX_PATH)

    with open(METADATA_PATH, "rb") as file:
        metadata = pickle.load(file)

    model = SentenceTransformer(MODEL_NAME)

    return index, metadata, model


def search(query, index, metadata, model):

    query_embedding = model.encode([query])
    query_embedding = query_embedding.astype("float32")

    distances, indices = index.search(
        query_embedding,
        TOP_K
    )

    results = []

    # Relevance threshold
    DISTANCE_THRESHOLD = 1.2

    for distance, index_number in zip(
        distances[0],
        indices[0]
    ):

        if distance <= DISTANCE_THRESHOLD:

            result = metadata[index_number].copy()

            result["distance"] = float(distance)

            results.append(result)

    return results

if __name__ == "__main__":

    index, metadata, model = load_resources()

    print("Legal RAG Retrieval System")
    print("---------------------------")

    query = input("\nEnter your question: ")

    results = search(
        query,
        index,
        metadata,
        model
    )

    print("\nRetrieved Results:")

    if not results:

        print("\nInformation not found in the provided legal documents.")

    else:

        for i, result in enumerate(results):

            print("\n==============================")
            print(f"Result {i + 1}")
            print(f"Source: {result['source']}")
            print(f"Page: {result['page']}")
            print(f"Distance: {result['distance']}")
            print("------------------------------")
            print(result["text"])