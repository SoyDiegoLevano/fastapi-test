# app/user/infrastructure/adapters/graphql/types.py
import strawberry
from app.user.domain.entities import User as UserEntity

@strawberry.type
class UserResponse:
    """
    Tipo de GraphQL para devolver datos del usuario.
    """
    user_id: int
    username: str
    email: str

    @classmethod
    def from_entity(cls, entity: UserEntity) -> "UserResponse":
        return cls(user_id=entity.user_id, username=entity.username, email=entity.email)


@strawberry.input
class UserCreateInput:
    """
    Input para crear un usuario.
    """
    username: str
    email: str
    password: str

@strawberry.input
class UserUpdateInput:
    """
    Input para actualizar un usuario.
    """
    user_id: int
    username: str
    email: str
    password: str
