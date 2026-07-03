from pathlib import Path

import aiofiles
from fastapi import UploadFile

UPLOAD_DIR = Path("app/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


class FileService:

    MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

    async def save_file(
        self,
        file: UploadFile,
    ) -> str:

        if file.content_type != "application/pdf":
            raise ValueError(
                "Only PDF files are allowed."
            )

        content = await file.read()

        if len(content) > self.MAX_FILE_SIZE:
            raise ValueError(
                "File size exceeds 5 MB."
            )

        file_path = UPLOAD_DIR / file.filename

        async with aiofiles.open(
            file_path,
            "wb",
        ) as f:
            await f.write(content)

        return file.filename