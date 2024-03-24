
from typing import Optional, List 
from pydantic import BaseModel, EmailStr, UUID4
from datetime import datetime

class UsuarioSchemaBase(BaseModel):
    id: Optional[UUID4] = None 
    data_inicial: Optional[str] = None
    data_atualizacao: Optional[str] = None
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

class UsuarioSchemaAddLaboratorio(UsuarioSchemaBase):
    list_laboratorios: List[UUID4]
class UsuarioSchemaAddProjeto(UsuarioSchemaBase):
    list_Projetos: List[UUID4]
class UsuarioSchemaLaboratoriosAndProjetos(UsuarioSchemaBase):
    laboratorios: Optional[List[LaboratorioSchema]]
    projetos: Optional[List[ProjetoSchema]]

class UsuarioSchemaUp(UsuarioSchemaBase):
    primeiro_nome: Optional[str]
    segundo_nome: Optional[str] 
    senha: Optional[str]
    email: Optional[EmailStr]
    matricula: Optional[int]
    tel: Optional[int]
    tag: Optional[int]