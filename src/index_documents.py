import os
import pickle

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

from pdf_loader import load_all_pdfs, create_chunks




INDEX_PATH = "vectorstore/legal.index"
METADATA_PATH = "vectorstore/metadata.pkl"

MODEL_NAME = "all-MiniLM-L6-v2"


def main():

    print("Loading legal documents...")

    pages = load_all_pdfs()

    print(f"Pages loaded: {len(pages)}")

    print("Creating chunks...")

    chunks = create_chunks(pages)

    print(f"Chunks created: {len(chunks)}")

    print("Loading embedding model...")

    model = SentenceTransformer(MODEL_NAME)

    texts = [chunk["text"] for chunk in chunks]

    print("Generating embeddings...")

    embeddings = model.encode(
        texts,
        show_progress_bar=True
    )

    embeddings = np.array(embeddings).astype("float32")

    print("Embedding shape:", embeddings.shape)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    print(f"Vectors stored in FAISS: {index.ntotal}")

    os.makedirs("vectorstore", exist_ok=True)

    faiss.write_index(index, INDEX_PATH)

    with open(METADATA_PATH, "wb") as file:
        pickle.dump(chunks, file)

    print("\nIndexing completed successfully.")

    print(f"FAISS index saved to: {INDEX_PATH}")
    print(f"Metadata saved to: {METADATA_PATH}")


if __name__ == "__main__":
    main()