# Day 15 - JWT Authentication

## Topics Covered

- JWT Authentication
- OAuth2 Password Flow
- Password Hashing with bcrypt
- python-jose
- Protected Routes
- Dependency Injection
- Token Expiry

## Endpoints

- POST /auth/register
- POST /auth/login
- GET /auth/me

## Run

```bash
uvicorn main:app --reload
```

## Features

- Password hashing
- JWT generation
- JWT verification
- Protected endpoints
- 401 Unauthorized handling