# app/user/infrastructure/adapters/graphql/schemas.py
import strawberry
from app.user.infrastructure.adapters.graphql.queries import Query as UserQuery
from app.user.infrastructure.adapters.graphql.mutations import Mutation as UserMutation

@strawberry.type
class Query(UserQuery):
    pass

@strawberry.type
class Mutation(UserMutation):
    pass


user_schema = strawberry.Schema(query=Query, mutation=Mutation)