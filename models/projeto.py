import uuid
from datetime import datetime
from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship
from __all_models import UsuarioProjetoAssociation, Usuario, Laboratorio

class Projeto(SQLModel, table=True):
    id: uuid.UUID = Field(primary_key=True, default=uuid.uuid4)
    titulo: str = Field(nullable=False)
    descricao: Optional[str] = Field(nullable=True)
    laboratorio_id: uuid.UUID = Field(foreign_key="laboratorio.id", nullable=False)
    autor_id: uuid.UUID = Field(foreign_key="usuario.id", nullable=False)
    data_inicial: Optional[datetime] = Field(default=datetime.now, nullable=False)
    data_up: Optional[datetime] = Field(default=datetime.now, nullable=False)
    membros: List[Usuario] = Relationship(back_populates="projetos", secondary=UsuarioProjetoAssociation)
    laboratorio: Laboratorio = Relationship(back_populates="projetos")
    autor: Usuario = Relationship(back_populates="projetos", uselist=False)