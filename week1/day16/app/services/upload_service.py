import os
import shutil

from fastapi import UploadFile

from app.ai.embeddings import EmbeddingService
from app.rag.chunker import Chunker
from app.rag.document_loader import DocumentLoader
from app.rag.vector_store import VectorStore


class UploadService:
    def __init__(self):
        self.upload_dir = "app/uploads"

        os.makedirs(
            self.upload_dir,
            exist_ok=True,
        )

        self.loader = DocumentLoader()

        self.chunker = Chunker(
            chunk_size=500,
            overlap=100,
        )

        self.embedding_service = EmbeddingService()

        self.vector_store = VectorStore()

    def upload_document(
        self,
        file: UploadFile,
    ):
        # -----------------------------
        # Save uploaded file
        # -----------------------------

        file_path = os.path.join(
            self.upload_dir,
            file.filename,
        )

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(
                file.file,
                buffer,
            )

        # -----------------------------
        # Load document
        # -----------------------------

        documents = self.loader.load(file_path)

        # -----------------------------
        # Chunk documents
        # -----------------------------

        chunks = []

        for document in documents:
            chunks.extend(
                self.chunker.split(document)
            )

        # -----------------------------
        # Generate embeddings
        # -----------------------------

        embeddings = self.embedding_service.embed_texts(
            [chunk.content for chunk in chunks]
        )

        # -----------------------------
        # Store vectors
        # -----------------------------

        self.vector_store.add_chunks(
            chunks,
            embeddings,
        )

        return {
            "success": True,
            "filename": file.filename,
            "documents": len(documents),
            "chunks": len(chunks),
            "message": "Document uploaded successfully."
        }