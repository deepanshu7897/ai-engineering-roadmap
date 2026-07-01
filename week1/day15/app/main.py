from datetime import datetime, timedelta
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

# -----------------------------
# Configuration
# -----------------------------

SECRET_KEY = "my_super_secret_key_for_demo_only"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)

fake_users_db = {}

# -----------------------------
# Models
# -----------------------------

class UserRegister(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


# -----------------------------
# Helper Functions
# -----------------------------

def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)


def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM,
    )


def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired token",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )

        username = payload.get("sub")

        if username is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    if username not in fake_users_db:
        raise credentials_exception

    return {"username": username}


# -----------------------------
# FastAPI
# -----------------------------

app = FastAPI(
    title="Day 15 - JWT Authentication"
)


# -----------------------------
# Routes
# -----------------------------

@app.get("/")
def home():
    return {"message": "JWT Authentication API"}


@app.post("/auth/register")
def register(user: UserRegister):

    if user.username in fake_users_db:
        raise HTTPException(
            status_code=400,
            detail="User already exists",
        )

    fake_users_db[user.username] = hash_password(
        user.password
    )

    return {"message": "User registered successfully"}


@app.post(
    "/auth/login",
    response_model=Token,
)
def login(
    form_data: Annotated[
        OAuth2PasswordRequestForm,
        Depends(),
    ]
):

    hashed_password = fake_users_db.get(
        form_data.username
    )

    if (
        hashed_password is None
        or not verify_password(
            form_data.password,
            hashed_password,
        )
    ):
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
        )

    access_token = create_access_token(
        {"sub": form_data.username}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }


@app.get("/auth/me")
def me(
    current_user: Annotated[
        dict,
        Depends(get_current_user),
    ]
):
    return current_user