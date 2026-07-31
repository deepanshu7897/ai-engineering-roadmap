from app.rag.chunk import Chunk
from app.rag.document import Document


class Chunker:
    def __init__(
        self,
        chunk_size: int = 500,
        overlap: int = 100,
    ):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def split(
        self,
        document: Document,
    ) -> list[Chunk]:

        text = document.content
        chunks = []

        start = 0

        while start < len(text):

            end = start + self.chunk_size

            chunk_text = text[start:end]

            chunk = Chunk(
                content=chunk_text,
                metadata=document.metadata.copy(),
            )

            chunks.append(chunk)

            start += self.chunk_size - self.overlap

        return chunks