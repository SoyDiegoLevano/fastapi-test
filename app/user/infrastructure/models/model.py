 # app/user/infrastructure/models/model.py
from sqlalchemy import Column, Integer, String
from passlib.context import CryptContext
from app.infrastructure.db.base import Base 

# Configuración de passlib para encriptar contraseñas usando bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserModel(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=True, unique=True)
    hashed_password = Column(String, nullable=False)

    def verify_password(self, plain_password: str) -> bool:
        """
        Verifica si la contraseña en texto plano coincide con la contraseña encriptada.
        """
        return pwd_context.verify(plain_password, self.hashed_password)

    def set_password(self, plain_password: str):
        """
        Encripta la contraseña en texto plano y la asigna al campo 'hashed_password'.
        """
        self.hashed_password = pwd_context.hash(plain_password)
