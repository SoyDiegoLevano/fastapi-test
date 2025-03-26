# app/product/infrastructure/adapters/graphql/types.py
import strawberry
from app.product.domain.entities import Product as ProductEntity

@strawberry.type
class ProductResponse:
    """
    Tipo de GraphQL para devolver datos de un producto.
    """
    id: int
    name: str
    price: float

    @classmethod
    def from_entity(cls, entity: ProductEntity) -> "ProductResponse":
        return cls(id=entity.id, name=entity.name, price=entity.price)


@strawberry.input
class ProductInput:
    """
    Input para crear un producto.
    """
    name: str
    price: float
