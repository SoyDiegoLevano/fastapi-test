# app/product/infrastructure/adapters/graphql/queries.py
import strawberry
from app.product.infrastructure.adapters.graphql.resolvers import ProductResolver
from app.product.infrastructure.adapters.graphql.types import ProductResponse

@strawberry.type
class Query:
    @strawberry.field
    async def product(self, id: int) -> ProductResponse:
        """
        Query para obtener un producto por su ID.
        """
        product_entity = await ProductResolver.get_product_by_id(id)
        return ProductResponse.from_entity(product_entity)
