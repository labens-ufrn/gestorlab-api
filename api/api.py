from fastapi import APIRouter
from api.endpoints import usuario, laboratorio

api_router = APIRouter()

api_router.include_router(usuario.router, prefix='/usuarios', tags=["usuarios"])
api_router.include_router(laboratorio.router, prefix='/laboratorios' ,tags=["laboratorios"])