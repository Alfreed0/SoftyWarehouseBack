from .base import TimeStampedModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Product(TimeStampedModel):
    __tablename__ = "Product"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    category = Column(String, nullable=False)
    unit = Column(String, nullable=False)
    value = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False)
    image = Column(String, nullable=True, default=None)

    items = relationship("Item", back_populates="product")
