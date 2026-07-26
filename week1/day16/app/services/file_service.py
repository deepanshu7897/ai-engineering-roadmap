from pathlib import Path

import aiofiles
from fastapi import UploadFile

from app.services.pdf_service import PDFService

UPLOAD_DIR = Path("app/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


class FileService:

    MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

    def __init__(self):
        self.pdf_service = PDFService()

    async def save_file(
        self,
        file: UploadFile,
    ) -> str:

        # Validate file type
        if file.content_type != "application/pdf":
            raise ValueError(
                "Only PDF files are allowed."
            )

        # Read file
        content = await file.read()

        # Validate file size
        if len(content) > self.MAX_FILE_SIZE:
            raise ValueError(
                "File size exceeds 5 MB."
            )

        # Save file
        file_path = UPLOAD_DIR / file.filename

        async with aiofiles.open(
            file_path,
            "wb",
        ) as f:
            await f.write(content)

        # -----------------------------
        # Extract text from PDF
        # -----------------------------
        text = self.pdf_service.extract_text(file_path)

        # -----------------------------
        # Split into chunks
        # -----------------------------
        chunks = self.pdf_service.chunk_text(text)

        # -----------------------------
        # Temporary logs (for testing)
        # -----------------------------
        print("=" * 60)
        print(f"PDF Uploaded : {file.filename}")
        print(f"Characters   : {len(text)}")
        print(f"Chunks       : {len(chunks)}")
        print("=" * 60)

        return file.filename