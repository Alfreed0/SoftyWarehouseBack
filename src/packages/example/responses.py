from pydantic import BaseModel
from utils.responses import SuccessResponse


class Token(BaseModel):
    access_token: str
    token_type: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCIXVCJ9...",
                    "token_type": "bearer",
                }
            ]
        }
    }


class TokenOut(SuccessResponse):
    payload: Token | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "status_code": 200,
                    "func": "post_login",
                    "message": "Success",
                    "payload": {
                        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCIXVCJ9...",
                        "token_type": "bearer",
                    },
                }
            ]
        }
    }
