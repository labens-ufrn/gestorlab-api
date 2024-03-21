from typing import Optional
from pydantic import BaseModel, EmailStr, UUID4
from datetime import datetime
from .usuario_schema import UsuarioSchemaBase

class LaboratorioSchema(BaseModel):
    id: Optional[UUID4] = None 
    coordenador_id: str
    nome: str
    descricao: str
    email: EmailStr
    data_inicial: datetime
    data_up: datetime
    coordenador: Optional[UsuarioSchemaBase]