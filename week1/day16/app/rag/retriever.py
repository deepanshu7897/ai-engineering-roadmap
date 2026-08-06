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
    ) -> dict:

        query_embedding = self.embedding_service.embed_text(query)

        results = self.vector_store.search(
            query_embedding=query_embedding,
            n_results=top_k,
        )

        documents = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]

        context = "\n\n".join(documents)

        sources = []
        seen = set()

        for metadata in metadatas:

            source = {
                "source": metadata.get("source"),
                "page": metadata.get("page"),
                "doc_type": metadata.get("doc_type"),
            }

            key = (
                source["source"],
                source["page"],
            )

            if key not in seen:
                seen.add(key)
                sources.append(source)

        return {
            "context": context,
            "sources": sources,
        }