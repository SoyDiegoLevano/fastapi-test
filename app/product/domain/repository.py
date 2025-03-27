# app/product/domain/repository.py
from abc import ABC, abstractmethod
from typing import List
from .entities import Product, ProductCreateDTO

class ProductRepository(ABC):
    @abstractmethod
    async def create(self, product_data: ProductCreateDTO) -> Product:
        pass

    @abstractmethod
    async def get_by_id(self, product_id: int) -> Product:
        pass

    @abstractmethod
    async def get_all(self) -> List[Product]:
        pass
