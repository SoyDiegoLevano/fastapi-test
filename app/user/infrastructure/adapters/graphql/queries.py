from typing import List
import strawberry
from app.user.infrastructure.adapters.graphql.resolvers import UserResolver
from app.user.infrastructure.adapters.graphql.types import UserResponse

@strawberry.type
class Query:
    @strawberry.field
    async def get_user_by_id(self, user_id: int) -> UserResponse:
        """
        Query para obtener un user por su ID.
        """
        user_entity = await UserResolver.get_user_by_id(user_id)
        return UserResponse.from_entity(user_entity)
    
    @strawberry.field
    async def get_all_users(self) -> List[UserResponse]:
        """
        Query para obtener todos los usuarios.
        """
        user_entities = await UserResolver.get_all_user()
        return [UserResponse.from_entity(user) for user in user_entities]