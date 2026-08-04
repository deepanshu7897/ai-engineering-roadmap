from fastapi import APIRouter, Depends, File, UploadFile

from app.core.dependencies import get_current_user
from app.models.user import User
from app.services.upload_service import UploadService

router = APIRouter(
    prefix="/rag",
    tags=["RAG"],
)

upload_service = UploadService()


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
):
    """
    Upload a document, process it and store its embeddings.
    """

    result = upload_service.upload_document(file)

    return result