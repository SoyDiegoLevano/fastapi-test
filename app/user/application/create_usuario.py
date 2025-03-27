# app/user/application/create_user.py
from app.user.domain.repository import UserRepository
from app.user.domain.entities import User, UserCreateDTO

class CreateUser:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, user_data: UserCreateDTO) -> User:
        """
        Caso de uso para crear un user.
        Llama al repositorio para persistirlo y devuelve la entidad de dominio resultante.
        """
        new_user = await self.user_repository.create_user(user_data)
        return new_user
