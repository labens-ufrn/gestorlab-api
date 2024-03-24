from typing import Optional, List
from pydantic import BaseModel, EmailStr, UUID4
from datetime import datetime
from .usuario_schema import UsuarioSchemaBase

class LaboratorioSchema(BaseModel):
    id: Optional[UUID4] = None 
    coordenador_id: Optional[UUID4] = None 
    nome: str
    descricao: str
    email: EmailStr
    data_inicial: Optional[datetime] = None 
    data_up: Optional[datetime] = None
    membros: Optional[List[UsuarioSchemaBase]] = None

    class Config:
        from_attributes = True

class LaboratorioSchemaCreate(BaseModel):
    nome: str
    descricao: str
    email: EmailStr
    membros: Optional[List[UUID4]] = None

class LaboratorioSchemaUp(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None
    email: Optional[EmailStr] = None
    membros: Optional[List[UUID4]] = None