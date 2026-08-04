import chromadb
from app.rag.chunk import Chunk


class VectorStore:
    def __init__(
        self,
        collection_name: str = "documents",
    ):
        self.client = chromadb.PersistentClient(
    path="./chroma_db",
)

        self.collection = self.client.get_or_create_collection(
            name=collection_name,
        )

    def add_chunks(
        self,
        chunks: list[Chunk],
        embeddings: list[list[float]],
    ) -> None:

        self.collection.add(
            ids=[str(i) for i in range(len(chunks))],
            documents=[chunk.content for chunk in chunks],
            metadatas=[chunk.metadata for chunk in chunks],
            embeddings=embeddings,
        )

    def search(
        self,
        query_embedding: list[float],
        n_results: int = 3,
    ):

        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results,
        )