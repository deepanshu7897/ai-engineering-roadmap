import asyncio
from pathlib import Path

from fastapi import APIRouter, HTTPException, UploadFile, File
from fastapi.responses import FileResponse, StreamingResponse

from app.services.file_service import FileService

router = APIRouter(
    prefix="/files",
    tags=["Files"],
)

service = FileService()


@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
):
    try:
        filename = await service.save_file(file)

        return {
            "message": "File uploaded successfully.",
            "filename": filename,
        }

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.get("/download/{filename}")
async def download_file(
    filename: str,
):
    file_path = Path("app/uploads") / filename

    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail="File not found.",
        )

    return FileResponse(
        path=file_path,
        media_type="application/pdf",
        filename=filename,
    )


async def fake_llm_stream():

    words = [
        "Hello",
        ", ",
        "this ",
        "is ",
        "a ",
        "streaming ",
        "response ",
        "from ",
        "FastAPI!",
    ]

    for word in words:
        yield word
        await asyncio.sleep(0.3)


@router.get("/stream")
async def stream():

    return StreamingResponse(
        fake_llm_stream(),
        media_type="text/plain",
    )