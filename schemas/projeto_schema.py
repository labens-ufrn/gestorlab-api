from typing import Optional
from pydantic import BaseModel, UUID4
from datetime import datetime
from .usuario_schema import UsuarioSchemaBase

class ProjetoSchema(BaseModel):
    id: Optional[UUID4] = None 
    titulo: str
    descricao: str
    autor_id: str 
    data_inicial: datetime
    data_up: datetime
    autor: Optional[UsuarioSchemaBase]