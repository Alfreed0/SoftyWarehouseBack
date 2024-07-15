from __future__ import annotations

from datetime import datetime, timedelta
from database import use_inventory_db
from utils.output import output_ERROR
from jose import jwt
from sqlalchemy import distinct

from .config import auth_settings
from .responses import Token
from .utils import verify_password

SECRET_KEY = auth_settings.SECRET_KEY
ALGORITHM = auth_settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = auth_settings.ACCESS_TOKEN_EXPIRE_MINUTES


def get_user(id: str):
    try:
        with use_inventory_db() as db:
            #db_user = db.query(User).filter(User.id == id).first()
            db_user = ""
            return db_user
    except Exception as e:
        output_ERROR(e, "get_user")
        raise e


def authenticate_user(user_id: str, password: str):
    try:
        db_user = get_user(user_id)
        return db_user
    except Exception as e:
        output_ERROR(e, "authenticate_user")
        raise e


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    try:
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    except Exception as e:
        output_ERROR(e, "create_access_token")
        raise e


def parse_permissions(permissions: list):
    try:
        perm_dict = {}
        for perm in permissions:
            tab, action = perm[0].split("-")
            perm_dict[tab] = perm_dict.get(tab, []) + [action]
        return perm_dict
    except Exception as e:
        output_ERROR(e, "parse_permissions")
        raise e


def get_token(user):
    try:
        pass
        return ""
    except Exception as e:
        output_ERROR(e, "get_token")
        raise e
