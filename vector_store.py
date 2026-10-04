import faiss # type: ignore
import numpy as np # type: ignore


def create_vector_store(embeddings):

    embeddings = np.array(embeddings).astype("float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    return index


if __name__ == "__main__":

    # Example embeddings
    embeddings = np.random.random((3, 384)).astype("float32")

    index = create_vector_store(embeddings)

    print("Number of vectors stored:", index.ntotal)
    print("Vector dimension:", index.d)