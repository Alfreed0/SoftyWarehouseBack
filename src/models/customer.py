from .base import TimeStampedModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Customer(TimeStampedModel):
    __tablename__ = "Customer"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    address = Column(String, nullable=False)
    notes = Column(String, nullable=True, default=None)
    status = Column(String, nullable=False)
    username = Column(String, nullable=False)

    orders = relationship(
        "Order",
        back_populates="customer",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
