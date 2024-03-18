from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime
from usuario_schema import UsuarioSchemaBase

class LaboratorioSchema(BaseModel):
    coordenador_id: str
    nome: str
    descricao: str
    email: EmailStr
    data_inicial: datetime
    data_up: datetime
    coordenador: Optional[UsuarioSchemaBase]