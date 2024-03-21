
from typing import Optional, List 
from pydantic import BaseModel, EmailStr, UUID4
from datetime import datetime

class UsuarioSchemaBase(BaseModel):
    id: Optional[UUID4] = None 
    primeiro_nome: str
    segundo_nome: str 
    email: EmailStr
    matricula: int
    tel: int
    tag: int

class Config:
    from_attributes = True

from schemas.laboratorio_schema import LaboratorioSchema
from schemas.projeto_schema import ProjetoSchema

class UsuarioSchemaCreate(UsuarioSchemaBase):
    senha: str

class UsuarioSchemaLaboratoriosAndProjetos(UsuarioSchemaBase):
    laboratorios: Optional[List[LaboratorioSchema]]
    projetos: Optional[List[ProjetoSchema]]

class UsuarioSchemaUp(UsuarioSchemaBase):
    primeiro_nome: Optional[str]
    segundo_nome: Optional[str] 
    email: Optional[EmailStr]
    matricula: Optional[str]
    tel: Optional[int]
    data_atualizacao: datetime
    tag: Optional[int]