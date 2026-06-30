import re

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ConfigDict, field_validator


class UserRegistration(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True
    )

    name: str
    email: str
    password: str
    age: int

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: str):
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        if not re.match(pattern, value):
            raise ValueError("Invalid email format")

        return value

    @field_validator("password")
    @classmethod
    def validate_password(cls, value: str):
        if len(value) < 8:
            raise ValueError(
                "Password must be at least 8 characters"
            )

        if not any(char.isdigit() for char in value):
            raise ValueError(
                "Password must contain at least one digit"
            )

        return value

    @field_validator("age")
    @classmethod
    def validate_age(cls, value: int):
        if value < 18:
            raise ValueError(
                "User must be at least 18 years old"
            )

        return value


class ErrorResponse(BaseModel):
    error: str
    detail: str | list
    code: str


app = FastAPI(
    title="FastAPI Day 14"
)


@app.exception_handler(HTTPException)
async def http_exception_handler(
    request: Request,
    exc: HTTPException,
):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": "HTTP Error",
            "detail": exc.detail,
            "code": str(exc.status_code),
        },
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError,
):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "error": "Validation Error",
            "detail": exc.errors(),
            "code": "422",
        },
    )


@app.exception_handler(Exception)
async def global_exception_handler(
    request: Request,
    exc: Exception,
):
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "detail": str(exc),
            "code": "500",
        },
    )


@app.get("/")
async def home():
    return {
        "message": "Validation API"
    }


@app.post(
    "/register",
    response_model=UserRegistration,
)
async def register(
    user: UserRegistration,
):
    return user


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    if user_id != 1:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    return {
        "id": 1,
        "name": "Deepanshu",
    }