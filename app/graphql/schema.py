"""
Este módulo define el esquema global de GraphQL, combinando las queries y mutations
de los módulos de producto y usuario.
"""

import strawberry
from app.product.infrastructure.adapters.graphql.schemas import product_schema
from app.user.infrastructure.adapters.graphql.schemas import user_schema

@strawberry.type
class Query(
    product_schema.query,  # Hereda las queries de producto
    user_schema.query,     # Hereda las queries de usuario
):
    """
    Esta Query global reúne las queries de todos los módulos.
    """

@strawberry.type
class Mutation(
    product_schema.mutation,  # Hereda las mutations de producto
    user_schema.mutation,     # Hereda las mutations de usuario
):
    """
    Esta Mutation global reúne las mutations de todos los módulos.
    """

schema = strawberry.Schema(query=Query, mutation=Mutation)
