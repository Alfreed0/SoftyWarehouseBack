from pydantic import BaseModel


class UserIn(BaseModel):
    id: str
    password: str


class UserData(BaseModel):
    id: str
    email: str
    name: str
    permissions: str


class TokenData(BaseModel):
    id: str | None = None
    name: str | None = None
    permission: dict | None = None
