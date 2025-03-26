# app/product/domain/repository.py
from abc import ABC, abstractmethod
from typing import List
from .entities import Product, ProductCreateDTO

class ProductRepository(ABC):
    @abstractmethod
    async def create(self, product: ProductCreateDTO) -> Product:
        """Crea un producto en la base de datos."""
        pass

    @abstractmethod
    async def get_by_id(self, product_id: int) -> Product:
        """Obtiene un producto por su ID."""
        pass

    @abstractmethod
    async def get_all(self) -> List[Product]:
        """Obtiene todos los productos."""
        pass
