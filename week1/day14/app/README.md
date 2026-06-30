# Day 14 - Validation, Error Handling & Response Models

## Topics Covered

- Pydantic v2 field_validator
- Pydantic v2 model_validator
- HTTPException
- Global Exception Handlers
- RequestValidationError
- Response Models

## Endpoints

- GET /
- POST /register
- GET /users/{user_id}

## Run

```bash
uvicorn main:app --reload
```

## Features

- Email Validation
- Password Strength Validation
- Confirm Password Validation
- Age Validation
- Consistent JSON Error Responses
- Global Exception Handling