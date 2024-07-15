from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime
from sqlalchemy import MetaData
from datetime import datetime
import pytz

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class TimeStampedModel(Base):
    __abstract__ = True

    created_at = Column(DateTime, default=datetime.now(pytz.utc))
    updated_at = Column(DateTime, nullable=True, default=None)
