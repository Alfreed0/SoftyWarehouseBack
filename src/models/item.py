from .base import TimeStampedModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Item(TimeStampedModel):
    __tablename__ = "Item"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    product_id = Column(
        Integer, ForeignKey("Product.id", ondelete="CASCADE"), nullable=False
    )
    order_id = Column(
        Integer, ForeignKey("Order.id", ondelete="CASCADE"), nullable=False
    )

    order = relationship("Order", back_populates="items")
    product = relationship("Product", back_populates="items")
