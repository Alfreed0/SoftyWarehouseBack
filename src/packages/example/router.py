from fastapi import APIRouter

from utils.exceptions import GeneralException

auth_router = APIRouter()

@auth_router.get("/token", )
async def get_token():
    try:
        x=str(1)
        y = ""
        return 2
    except Exception as e:
        GeneralException(e, "get_token").show_msg()  


