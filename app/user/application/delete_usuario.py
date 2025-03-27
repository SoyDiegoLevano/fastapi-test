from app.user.domain.repository import UserRepository

class DeleteUser:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, user_id: int) -> bool:
        """
        Caso de uso para eliminar un usuario.
        Llama al repositorio para eliminar el usuario y devuelve True si se eliminó correctamente,
        o False en caso contrario.
        """
        result = await self.user_repository.delete_user(user_id)
        return result
