from fastapi import APIRouter

from packages.example.router import auth_router


router = APIRouter()

router.include_router(auth_router, prefix="/auth")