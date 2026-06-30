# Day 14 - Validation & Error Handling

## Topics

- field_validator
- HTTPException
- Global Exception Handlers
- RequestValidationError
- Response Models

## Endpoints

GET /

POST /register

GET /users/{id}

## Run

```bash
uvicorn main:app --reload
```

## Result

Implemented request validation, consistent JSON error responses, and global exception handling using FastAPI and Pydantic.