# app/product/infrastructure/adapters/graphql/schemas.py
import strawberry
from app.product.infrastructure.adapters.graphql.queries import Query as ProductQuery
from app.product.infrastructure.adapters.graphql.mutations import Mutation as ProductMutation

@strawberry.type
class Query(ProductQuery):
    pass

@strawberry.type
class Mutation(ProductMutation):
    pass

product_schema = strawberry.Schema(query=Query, mutation=Mutation)
