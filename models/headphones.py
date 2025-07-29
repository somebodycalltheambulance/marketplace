from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from db.session import Base

class Headphone(Base):
    __tablename__ = "headphones"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    brand = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"))
    description = Column(String, nullable=True)

    category = relationship("Category")

    def __str__(self):
        return self.name
