from app.ai.embeddings import EmbeddingService
from app.rag.vector_store import VectorStore


class Retriever:
    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.vector_store = VectorStore()

    def retrieve(
        self,
        query: str,
        top_k: int = 3,
    ) -> str:

        query_embedding = self.embedding_service.embed_text(query)

        results = self.vector_store.search(
            query_embedding=query_embedding,
            n_results=top_k,
        )

        documents = results["documents"][0]

        context = "\n\n".join(documents)

        return context