from fastapi import APIRouter
from api.endpoints import usuario

api_router = APIRouter()

api_router.include_router(usuario.router, prefix='/usuarios', tags=["usuarios"])