# app/product/infrastructure/adapters/graphql/mutations.py
import strawberry
from app.product.infrastructure.adapters.graphql.resolvers import ProductResolver
from app.product.infrastructure.adapters.graphql.types import ProductInput, ProductResponse

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_product(self, product_data: ProductInput) -> ProductResponse:
        """
        Mutación para crear un nuevo producto.
        """
        product_entity = await ProductResolver.create_product(product_data)
        return ProductResponse.from_entity(product_entity)
