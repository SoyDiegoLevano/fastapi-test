# app/product/application/get_product.py
from app.product.domain.repository import ProductRepository
from app.product.domain.entities import Product

class GetProduct:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    async def execute(self, product_id: int) -> Product:
        """
        Caso de uso para obtener un producto por ID.
        """
        product = await self.product_repository.get_by_id(product_id)
        return product
 