from app.ai.gemini_client import GeminiClient
from app.rag.document_loader import DocumentLoader
from app.rag.chunker import Chunker
from app.rag.vector_store import VectorStore


def main():
    loader = DocumentLoader()
    documents = loader.load("sample_docs/sample.pdf")

    chunker = Chunker(
        chunk_size=500,
        overlap=100,
    )

    all_chunks = []

    for document in documents:
        all_chunks.extend(chunker.split(document))

    print(f"Total Chunks: {len(all_chunks)}")

    gemini = GeminiClient()

    embeddings = gemini.embed_batch(
        [chunk.content for chunk in all_chunks],
        task_type="RETRIEVAL_DOCUMENT",
    )

    print(f"Generated {len(embeddings)} embeddings")

    vector_store = VectorStore()

    vector_store.add_chunks(
        all_chunks,
        embeddings,
    )

    print("Chunks stored successfully!")

    query = "Software Engineer"

    query_embedding = gemini.embed_text(
        query,
        task_type="RETRIEVAL_QUERY",
    )

    results = vector_store.search(
        query_embedding=query_embedding,
        n_results=2,
    )

    print("\nSearch Results:\n")

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    for index, (doc, meta) in enumerate(zip(documents, metadatas), start=1):
        print("=" * 60)
        print(f"Result {index}")
        print(meta)
        print()
        print(doc[:300])
        print()


if __name__ == "__main__":
    main()