# app/product/application/create_product.py
from app.product.domain.repository import ProductRepository
from app.product.domain.entities import Product, ProductCreateDTO

class CreateProduct:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    async def execute(self, product_data: ProductCreateDTO) -> Product:
        """
        Caso de uso para crear un producto.
        Llama al repositorio para persistirlo y devuelve la entidad de dominio resultante.
        """
        new_product = await self.product_repository.create(product_data)
        return new_product
