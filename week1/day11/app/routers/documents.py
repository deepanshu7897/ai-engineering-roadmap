from fastapi import APIRouter, HTTPException

from app.schemas.document import (
    DocumentCreate,
    DocumentResponse,
)

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)

documents = []


@router.get("/", response_model=list[DocumentResponse])
def get_all_documents():
    return documents


@router.get("/{doc_id}", response_model=DocumentResponse)
def get_document(doc_id: int):
    if doc_id > len(documents) or doc_id <= 0:
        raise HTTPException(status_code=404, detail="Document not found")

    return documents[doc_id - 1]


@router.post("/", response_model=DocumentResponse)
def create_document(document: DocumentCreate):
    new_doc = {
        "id": len(documents) + 1,
        "title": document.title,
        "content": document.content,
    }

    documents.append(new_doc)

    return new_doc


@router.put("/{doc_id}", response_model=DocumentResponse)
def update_document(doc_id: int, document: DocumentCreate):
    if doc_id > len(documents) or doc_id <= 0:
        raise HTTPException(status_code=404, detail="Document not found")

    updated = {
        "id": doc_id,
        "title": document.title,
        "content": document.content,
    }

    documents[doc_id - 1] = updated

    return updated


@router.delete("/{doc_id}")
def delete_document(doc_id: int):
    if doc_id > len(documents) or doc_id <= 0:
        raise HTTPException(status_code=404, detail="Document not found")

    documents.pop(doc_id - 1)

    return {"message": "Document deleted successfully"}