# app/product/infrastructure/adapters/graphql/resolvers.py
from app.infrastructure.db.db_config import get_db
from app.product.infrastructure.adapters.sqlalchemy_product_repository import SQLAlchemyProductRepository
from app.product.application.create_product import CreateProduct
from app.product.application.get_product import GetProduct
from app.product.domain.entities import Product
from .types import ProductInput

class ProductResolver:
    @staticmethod
    async def create_product(product_data: ProductInput) -> Product:
        """
        Resolver que crea un producto usando el caso de uso 'CreateProduct'.
        """
        async for session in get_db():
            product_repo = SQLAlchemyProductRepository(session)
            use_case = CreateProduct(product_repo)
            new_product = await use_case.execute(product_data)
            return new_product

    @staticmethod
    async def get_product_by_id(product_id: int) -> Product:
        """
        Resolver que obtiene un producto por ID usando el caso de uso 'GetProduct'.
        """
        async for session in get_db():
            product_repo = SQLAlchemyProductRepository(session)
            use_case = GetProduct(product_repo)
            product = await use_case.execute(product_id)
            return product
