# app/graphql/schema.py
import strawberry
from app.product.infrastructure.adapters.graphql.queries import Query as ProductQuery
from app.product.infrastructure.adapters.graphql.mutations import Mutation as ProductMutation

@strawberry.type
class Query(ProductQuery):
    """
    Extendemos con más queries de otros módulos si es necesario.
    """
    pass

@strawberry.type
class Mutation(ProductMutation):
    """
    Extendemos con más mutations de otros módulos si es necesario.
    """
    pass

schema = strawberry.Schema(query=Query, mutation=Mutation)
