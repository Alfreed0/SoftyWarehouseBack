from pydantic import BaseModel
from starlette import status


class ResponseModel(BaseModel):
    message: str
    status_code: str
    func: str = None
    payload: dict = None


class SuccessResponse(ResponseModel):
    status_code: int = status.HTTP_200_OK
    message: str = "Success"


class InternalServerErrorResponse(ResponseModel):
    status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    message: str = "Internal Server Error"
