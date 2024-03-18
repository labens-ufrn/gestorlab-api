from typing import Optional, List 

from pydantic import BaseModel, EmailStr
from datetime import datetime

from schemas.laboratorio_schema import LaboratorioSchema
from schemas.projeto_schema import ProjetoSchema

#Base dos usuarios
class UsuarioSchemaBase(BaseModel):
    id: Optional[str] = None
    primeiro_nome: str
    segundo_nome: str 
    email: EmailStr
    matricula: str
    tel: int
    data_inicial: datetime
    data_atualizacao: datetime
    tag: int

    class Config:
        from_attributes = True


class UsuarioSchemaCreate(UsuarioSchemaBase):
    senha: str

class UsuarioSchemaLaboratorios(UsuarioSchemaBase):
    laboratorios: Optional[List[LaboratorioSchema]]

class UsuarioSchemaProjetos(UsuarioSchemaBase):
    projetos: Optional[List[ProjetoSchema]]

class UsuarioSchemaUp(UsuarioSchemaBase):
    primeiro_nome: Optional[str]
    segundo_nome: Optional[str] 
    email: Optional[EmailStr]
    matricula: Optional[str]
    tel: Optional[int]
    data_atualizacao: datetime
    tag: Optional[int]