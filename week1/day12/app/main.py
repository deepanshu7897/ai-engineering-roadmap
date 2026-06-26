from typing import Annotated

from fastapi import Depends, FastAPI

from dependencies import (
    get_db,
    verify_api_key,
)

app = FastAPI(
    title="FastAPI Day 12"
)


@app.get("/")
def home():
    return {
        "message": "Dependency Injection Demo"
    }


@app.get("/documents")
def get_documents(
    db: Annotated[
        dict,
        Depends(get_db),
    ],
    _: Annotated[
        None,
        Depends(verify_api_key),
    ],
):
    return db["documents"]


@app.post("/documents")
def create_document(
    title: str,
    db: Annotated[
        dict,
        Depends(get_db),
    ],
    _: Annotated[
        None,
        Depends(verify_api_key),
    ],
):
    db["documents"].append(title)

    return {
        "message": "Created",
        "documents": db["documents"],
    }


@app.put("/documents/{index}")
def update_document(
    index: int,
    title: str,
    db: Annotated[
        dict,
        Depends(get_db),
    ],
    _: Annotated[
        None,
        Depends(verify_api_key),
    ],
):
    if index >= len(db["documents"]):
        return {
            "error": "Not Found"
        }

    db["documents"][index] = title

    return db["documents"]


@app.delete("/documents/{index}")
def delete_document(
    index: int,
    db: Annotated[
        dict,
        Depends(get_db),
    ],
    _: Annotated[
        None,
        Depends(verify_api_key),
    ],
):
    if index >= len(db["documents"]):
        return {
            "error": "Not Found"
        }

    db["documents"].pop(index)

    return {
        "message": "Deleted"
    }