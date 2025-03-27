from app.user.domain.repository import UserRepository
from app.user.domain.entities import User

class GetUser:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, user_id: int) -> User:
        """
        Caso de uso para traer un usuario por su id
        """
        result = await self.user_repository.get_user_by_id(user_id)
        return result
