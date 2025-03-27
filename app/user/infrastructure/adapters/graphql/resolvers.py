# app/user/infrastructure/adapters/graphql/resolvers.py
from typing import List
from app.infrastructure.db.db_config import get_db
from app.user.infrastructure.adapters.sqlalchemy_user_repository import SQLAlchemyUserRepository
from app.user.application.create_usuario import CreateUser
from app.user.application.update_usuario import UpdateUser
from app.user.application.delete_usuario import DeleteUser
from app.user.application.get_usuario import GetUser
from app.user.application.getall_usuario import GetAllUsers

from app.user.domain.entities import User
from.types import UserCreateInput, UserUpdateInput


class UserResolver:
    @staticmethod
    async def create_user(user_data: UserCreateInput) -> User:
        """
        Resolver que crea un usuario usando el caso de uso 'CreateUser'.
        """
        async for session in get_db():
            user_repo = SQLAlchemyUserRepository(session)
            use_case = CreateUser(user_repo)
            new_user = await use_case.execute(user_data)
            return new_user
        
    @staticmethod
    async def update_user(user_data: UserUpdateInput) -> User:
        """
        Resolver que crea un usuario usando el caso de uso 'CreateUser'.
        """
        async for session in get_db():
            user_repo = SQLAlchemyUserRepository(session)
            use_case = UpdateUser(user_repo)
            new_user = await use_case.execute(user_data)
            return new_user
        
    @staticmethod
    async def delete_user(user_id: int) -> bool:
        """
        Resolver que elimina un usuario usando el caso de uso 'DeleteUser'.
        """
        async for session in get_db():
            user_repo = SQLAlchemyUserRepository(session)
            use_case = DeleteUser(user_repo)
            result = await use_case.execute(user_id)
            return result


    @staticmethod
    async def get_user_by_id(user_id: int) -> User:
        """
        Resolver que obtiene un usero por ID usando el caso de uso 'GetUser'.
        """
        async for session in get_db():
            user_repo = SQLAlchemyUserRepository(session)
            use_case = GetUser(user_repo)
            user = await use_case.execute(user_id)
            return user
    
    @staticmethod

    async def get_all_user() -> List[User]:
        """
        Resolver que obtiene una lista de usuarios con el caso de uso 'GetAllUser'.
        """
        async for session in get_db():
            user_repo = SQLAlchemyUserRepository(session)
            use_case = GetAllUsers(user_repo)
            user = await use_case.execute()
            return user
        
    
