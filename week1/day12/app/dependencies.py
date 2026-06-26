from fastapi import Header, HTTPException


def get_db():
    db = {
        "documents": []
    }

    try:
        yield db

    finally:
        db.clear()


def verify_api_key(
    x_api_key: str = Header(None),
):
    if x_api_key != "secret123":
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API Key",
        )