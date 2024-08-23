from pydantic import BaseModel
from sqlalchemy import Column, Integer, Boolean, Double, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Category(Base):
    __tablename__ = 'categories'

    category_id = Column(Integer, primary_key=True)
    category_name = Column(String)
    description = Column(String)

    products = relationship("Product", back_populates="category")

    def __repr__(self):
        return f"Category: {self.category_id}){self.category_name}"


class Product(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True)
    product_name = Column(String)
    supplier_id = Column(Integer)
    category_id = Column(Integer, ForeignKey('categories.category_id'))
    quantity_per_unit = Column(String)
    unit_price = Column(Double)
    units_in_stock = Column(Integer)
    units_on_order = Column(Integer)
    reorder_level = Column(Integer)
    discontinued = Column(Boolean)

    category = relationship("Category", back_populates="products")

    def __repr__(self):
        return f"Product: {self.product_id}){self.product_name}"


class ProductBase(BaseModel):
    product_id: int
    product_name: str
    supplier_id: int
    category_id: int
    quantity_per_unit: str
    unit_price: float
    units_in_stock: int
    units_on_order: int
    reorder_level: int
    discontinued: bool

    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    category_id: int
    category_name: str
    description: str

    class Config:
        orm_mode = True
