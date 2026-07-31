from app.rag.chunker import Chunker
from app.rag.document_loader import DocumentLoader


def main():
    loader = DocumentLoader()

    documents = loader.load("sample_docs/sample.pdf")

    chunker = Chunker(
        chunk_size=500,
        overlap=100,
    )

    for document in documents:

        chunks = chunker.split(document)

        print(f"\nTotal Chunks: {len(chunks)}\n")

        for index, chunk in enumerate(chunks, start=1):
            print("=" * 60)
            print(f"Chunk {index}")
            print("-" * 60)
            print("Metadata:")
            print(chunk.metadata)
            print("\nContent Preview:")
            print(chunk.content[:200])
            print()


if __name__ == "__main__":
    main()