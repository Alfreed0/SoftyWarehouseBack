from .base import TimeStampedModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Delivery(TimeStampedModel):
    __tablename__ = "Delivery"
    id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    identification = Column(String, nullable=False)
    address = Column(String, nullable=False)
    city = Column(String, nullable=False)
    province = Column(String, nullable=False)
    order_id = Column(
        Integer, ForeignKey("Order.id", ondelete="CASCADE"), nullable=False
    )

    order = relationship("Order", back_populates="delivery")
