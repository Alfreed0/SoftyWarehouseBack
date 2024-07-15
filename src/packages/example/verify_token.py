from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from jose.exceptions import ExpiredSignatureError, JWTError
from database import use_warehouse_db
from models import User

from .schemas import TokenData
from .config import auth_settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token")
SECRET_KEY = auth_settings.SECRET_KEY
ALGORITHM = auth_settings.ALGORITHM


class TokenVerifier:
    def __init__(self, permission: list[str], token: str = Depends(oauth2_scheme)):
        self.tab, self.action = permission.split("-")

    async def __call__(self, token: str = Depends(oauth2_scheme)):
        return await self.verify_token(token)

    async def verify_token(self, token: str):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            permission: list = payload.get("permission")
            val_permission = self.action in permission.get(self.tab, [])
        except Exception as e:
            pass

        """ except ExpiredSignatureError:
            e = ExpiredTokenException("verify_token")
            output_ERROR(e)
            raise HTTPException(status_code=e.status_code, detail=e.message)

        except JWTError:
            e = InvalidTokenException("verify_token")
            output_ERROR(e)
            raise HTTPException(status_code=e.status_code, detail=e.message)

        except CustomException as e:
            output_ERROR(e)
            raise HTTPException(status_code=e.status_code, detail=e.message)

        except Exception as e:
            output_ERROR(e, "verify_token")
            raise HTTPException(status_code=e.status_code, detail=e.message) """
