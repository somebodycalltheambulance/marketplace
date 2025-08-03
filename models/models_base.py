from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean
from sqlalchemy.orm import relationship
from db.session import Base
from sqlalchemy.ext.declarative import declared_attr

class ProductBase:
    __abstract__ = True

    @declared_attr
    def id(cls):
        return Column(Integer, primary_key=True)

    @declared_attr
    def name(cls):
        return Column(String, nullable=False)

    @declared_attr
    def brand(cls):
        return Column(String, nullable=True)

    @declared_attr
    def price(cls):
        return Column(Float, nullable=False)

    @declared_attr
    def category_id(cls):
        return Column(Integer, ForeignKey("categories.id"))

    @declared_attr
    def description(cls):
        return Column(String, nullable=True)

    @declared_attr
    def category(cls):
        return relationship("Category")

# Смартфоны
class Phone(ProductBase, Base):
    __tablename__ = "phones"
    ram = Column(Integer, nullable=False)
    storage = Column(Integer, nullable=False)
    Color = Column(String, nullable=False)
    # Если надо, сюда можно добавить специфичные поля


# Наушники
class Headphone(ProductBase, Base):
    __tablename__ = "headphones"
    noise_cancelling = Column(Boolean)


# Аксессуары
class Accessory(ProductBase, Base):
    __tablename__ = "accessories"
    type = Column(String)
