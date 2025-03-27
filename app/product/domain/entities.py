# app/product/domain/entities.py
from pydantic import BaseModel

# Entidad de dominio

class Product(BaseModel):
    id: int
    name: str
    price: float

    class Config:
        from_attributes = True

#    @classmethod
#    def from_orm(cls, orm_model) -> "Product":
#        """Convierte un modelo de ORM (SQLAlchemy) a la entidad de dominio."""
#       return cls(
#            id=orm_model.id,
#            name=orm_model.name,
#            price=orm_model.price
#        )
#   Solo crearlo si es necesario un proceso de algun atributo antes de guardarlo

# DTO para creación
class ProductCreateDTO(BaseModel):
    name: str
    price: float

# DTO para actualización (opcional)
#class ProductUpdateDTO(BaseModel):
#    id: int
#    name: str
#    price: float
