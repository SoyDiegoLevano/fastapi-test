# User/Application/CreateUserHandler.py

from passlib.context import CryptContext
from User.Domain.user import User
from infrastructure.config import ACCESS_TOKEN_EXPIRE_MINUTES
# Nota: Se espera que el repositorio se inyecte (implementado en Infrastructure)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_user(username: str, password: str, user_repo) -> str:
    """Orquesta la lógica para registrar un nuevo usuario."""
    hashed_password = get_password_hash(password)
    user_repo.create_user(username, hashed_password)
    return "Usuario registrado"
