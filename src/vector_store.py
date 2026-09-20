import faiss
import numpy as np


# Each vector has 384 dimensions
dimension = 384

# Create a FAISS index
index = faiss.IndexFlatL2(dimension)


# Create some example vectors
vectors = np.random.random((5, dimension)).astype("float32")


# Add vectors to the index
index.add(vectors)


print("Vectors stored:", index.ntotal)


# Create a query vector
query_vector = np.random.random((1, dimension)).astype("float32")


# Search for the 2 closest vectors
distances, indices = index.search(query_vector, 2)


print("\nClosest vector indices:")
print(indices)

print("\nDistances:")
print(distances)