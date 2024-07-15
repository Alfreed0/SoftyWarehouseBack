import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from .config import postgres_settings


url = URL.create(
    drivername=postgres_settings.POSTGRES_DRIVER,
    username=postgres_settings.POSTGRES_USER,
    host=postgres_settings.POSTGRES_HOST,
    database=postgres_settings.POSTGRES_DB,
    password=postgres_settings.POSTGRES_PASSWORD,
    port=postgres_settings.POSTGRES_PORT,
)

engine = create_engine(url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class WarehouseDBSession:
    def __enter__(self) -> Session:
        self.db = SessionLocal()
        return self.db

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type is not None:
                self.db.rollback()
        except sqlalchemy.exc.SQLAlchemyError:
            pass
        finally:
            self.db.close()


def use_warehouse_db():
    return WarehouseDBSession()
