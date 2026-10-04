from sentence_transformers import SentenceTransformer # type: ignore

# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(chunks):
    embeddings = model.encode(chunks)

    return embeddings


if __name__ == "__main__":

    test_chunks = [
        "Machine learning is a branch of artificial intelligence.",
        "Deep learning uses neural networks.",
        "Pizza is a popular food."
    ]

    embeddings = create_embeddings(test_chunks)

    print("Number of chunks:", len(embeddings))
    print("Embedding size:", len(embeddings[0]))