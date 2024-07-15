from .base import TimeStampedModel
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship


class Payment(TimeStampedModel):
    __tablename__ = "Payment"
    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Integer, nullable=False)
    method = Column(String, nullable=False)
    order_id = Column(
        Integer, ForeignKey("Order.id", ondelete="CASCADE"), nullable=False
    )

    order = relationship("Order", back_populates="payments")
