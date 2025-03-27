from typing import List
from app.user.domain.repository import UserRepository
from app.user.domain.entities import User

class GetAllUsers:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self) -> List[User]:
        """
        Caso de uso para obtener todos los usuarios.
        Llama al repositorio para traer la lista completa de usuarios.
        """
        result = await self.user_repository.get_all_user()
        return result
