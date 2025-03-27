import strawberry 
from app.user.infrastructure.adapters.graphql.resolvers import UserResolver
from app.user.infrastructure.adapters.graphql.types import UserCreateInput, UserUpdateInput, UserResponse

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_user(self, user_data: UserCreateInput) -> UserResponse:
        return await UserResolver.create_user(user_data)

    @strawberry.mutation
    async def update_user(self, user_data: UserUpdateInput) -> UserResponse:
        return await UserResolver.update_user(user_data)
    
    @strawberry.mutation
    async def delete_user(self, user_id: int) -> bool:
        return await UserResolver.delete_user(user_id)