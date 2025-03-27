# app/product/domain/entities.py
from pydantic import BaseModel
# Entidad de dominio

class User(BaseModel):
    user_id: int
    username: str
    email: str
    hashed_password: str #Hace referencia a la entidad como esta en la model, no cambiar nombre atributos
    
    class Config:
        from_attributes = True

# DTO para creación
class UserCreateDTO(BaseModel):
    username: str
    email: str
    password: str

# DTO para actualizar
class UserUpdateDTO(BaseModel):
    user_id: int
    username: str
    email: str
    password: str





