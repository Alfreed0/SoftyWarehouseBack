from .base import TimeStampedModel
from sqlalchemy import Column, Integer, String


class User(TimeStampedModel):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)
