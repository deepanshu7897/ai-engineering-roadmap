import numpy as np

from app.ai.gemini_client import GeminiClient


class SemanticSearch:

    def __init__(self):
        self.client = GeminiClient()

        self.documents = []
        self.embeddings = []

    # -----------------------------
    # Add Documents
    # -----------------------------

    def add_documents(
        self,
        documents: list[str],
    ):

        self.documents.extend(documents)

        embeddings = self.client.embed_batch(
            documents,
            task_type="RETRIEVAL_DOCUMENT",
        )

        self.embeddings.extend(embeddings)

    # -----------------------------
    # Cosine Similarity
    # -----------------------------

    def cosine_similarity(
        self,
        a: list[float],
        b: list[float],
    ) -> float:

        a = np.array(a)
        b = np.array(b)

        return np.dot(a, b) / (
            np.linalg.norm(a) * np.linalg.norm(b)
        )

    # -----------------------------
    # Semantic Search
    # -----------------------------

    def search(
        self,
        query: str,
        top_k: int = 5,
    ):

        query_embedding = self.client.embed_text(
            query,
            task_type="RETRIEVAL_QUERY",
        )

        scores = []

        for doc, embedding in zip(
            self.documents,
            self.embeddings,
        ):

            similarity = self.cosine_similarity(
                query_embedding,
                embedding,
            )

            scores.append(
                (
                    doc,
                    similarity,
                )
            )

        scores.sort(
            key=lambda x: x[1],
            reverse=True,
        )

        return scores[:top_k]