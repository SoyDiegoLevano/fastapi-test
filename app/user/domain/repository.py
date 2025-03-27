from abc import ABC, abstractmethod
from typing import List
from .entities import User, UserCreateDTO, UserUpdateDTO

class UserRepository(ABC):
    @abstractmethod
    async def create_user(self, user_data: UserCreateDTO) -> User:
        pass

    @abstractmethod
    async def update_user(self, user_data: UserUpdateDTO) -> User:
        pass

    @abstractmethod
    async def delete_user(self, user_id: int) -> bool:
        pass

    @abstractmethod
    async def get_user_by_id(self, user_id: int) -> User:
        pass

    @abstractmethod
    async def get_all_user(self) -> List[User]:
        pass
