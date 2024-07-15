from passlib.context import CryptContext
import random
import string

from .config import auth_settings

SECRET_KEY = auth_settings.SECRET_KEY
SALT = auth_settings.SALT

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    salted_password = plain_password + SALT
    return pwd_context.verify(salted_password, hashed_password)


def get_password_hash(password):
    salted_password = password + SALT
    return pwd_context.hash(salted_password)


def generate_base_password(length: int = 8):
    chars = string.ascii_letters + string.digits

    password = "".join(random.choice(chars) for i in range(length))
    return password
