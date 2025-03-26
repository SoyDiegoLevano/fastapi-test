# User/Application/LoginUserHandler.py
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from typing import Optional
import jwt
from passlib.context import CryptContext
from User.Domain.user import User


# Cargar variables de entorno
load_dotenv()

# Obtener la URL de la base de datos desde .env
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def login_user(username: str, password: str, user_repo) -> str:
    """Orquesta la lógica de login."""
    user = user_repo.get_user_by_username(username)
    if not user or not verify_password(password, user.password):
        raise Exception("Credenciales inválidas")
    return create_access_token({"username": user.username})
