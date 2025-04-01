# app/product/infrastructure/models/model.py
from sqlalchemy import Column, Integer, String, Float
from app.infrastructure.db.base import Base 

class ProductModel(Base):
    __tablename__ = "products"
 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    test = Column(String, nullable=True)
   