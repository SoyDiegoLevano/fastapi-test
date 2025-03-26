# app/product/infrastructure/adapters/sqlalchemy_product_repository.py
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.product.domain.repository import ProductRepository
from app.product.domain.entities import Product, ProductCreateDTO
from app.product.infrastructure.models.model import ProductModel

class SQLAlchemyProductRepository(ProductRepository):
    def __init__(self, session: Session):
        self.session = session

    async def create(self, product_data: ProductCreateDTO) -> Product: # Indica que lo que devuelve es un Product
        # Creamos el modelo ORM
        product_orm = ProductModel(
            name=product_data.name,
            price=product_data.price
        )
        self.session.add(product_orm)
        await self.session.commit()
        await self.session.refresh(product_orm)

        # Convertimos el modelo (como esta en la base de datos / como lo usa el orm) a entidad de dominio (como lo usamos en la app)
        # return Product.from_orm(product_orm)
        return Product.model_validate(product_orm)

    async def get_by_id(self, product_id: int) -> Product:
        stmt = select(ProductModel).where(ProductModel.id == product_id)
        result = await self.session.execute(stmt)
        product_orm = result.scalars().first()

        if not product_orm:
            raise ValueError(f"Product with ID {product_id} not found.")

        return Product.model_validate(product_orm)

    async def get_all(self) -> list[Product]:
        stmt = select(ProductModel)
        result = await self.session.execute(stmt)
        product_orms = result.scalars().all()

        #return [Product.from_orm(p) for p in product_orms]
        return [Product.model_validate(p) for p in product_orms]
