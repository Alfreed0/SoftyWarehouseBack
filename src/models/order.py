from .base import TimeStampedModel
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class Order(TimeStampedModel):
    __tablename__ = "Order"
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(
        Integer, ForeignKey("Customer.id", ondelete="CASCADE"), nullable=False
    )
    status = Column(String, nullable=False)
    notes = Column(String, nullable=True, default=None)
    total = Column(Integer, nullable=False)
    amount_paid = Column(Integer, nullable=False)

    customer = relationship("Customer", back_populates="orders")
    items = relationship(
        "Item",
        back_populates="order",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )

    delivery = relationship(
        "Delivery",
        back_populates="order",
        uselist=False,
        cascade="all, delete-orphan",
        passive_deletes=True,
    )

    payments = relationship(
        "Payment",
        back_populates="order",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
