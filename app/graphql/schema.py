# app/graphql/schema.py
# app/graphql/schema.py
import strawberry
from app.product.infrastructure.adapters.graphql.schemas import product_schema


# Creamos una Query global combinando las queries individuales
@strawberry.type
class Query(
    product_schema.query,   # Hereda de ProductQuery
):
    """
    Esta Query global reúne las queries de todos los módulos.
    """

# Creamos una Mutation global combinando las mutaciones individuales
@strawberry.type
class Mutation(
    product_schema.mutation,  # Hereda de ProductMutation
):
    """
    Esta Mutation global reúne las mutaciones de todos los módulos.
    """

# Definimos el schema global utilizando las Query y Mutation globales
schema = strawberry.Schema(query=Query, mutation=Mutation)

