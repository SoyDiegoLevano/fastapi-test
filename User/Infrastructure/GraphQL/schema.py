# User/Infrastructure/GraphQL/schema.py

import strawberry
from .query import Query as UserQuery
from .mutation import Mutation as UserMutation

schema = strawberry.Schema(query=UserQuery, mutation=UserMutation)
