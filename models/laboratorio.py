import uuid
from datetime import datetime
from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship
from __all_models import UsuarioLaboratorioAssociation, Usuario

class Laboratorio(SQLModel, table=True):
    id: uuid.UUID = Field(primary_key=True, default=uuid.uuid4)
    nome: str = Field(nullable=False)
    descricao: Optional[str] = Field(nullable=True)
    email: Optional[str] = Field(nullable=True)
    data_inicial: Optional[datetime] = Field(default=datetime.now, nullable=False)
    data_up: Optional[datetime] = Field(default=datetime.now, nullable=False)
    usuarios: List[Usuario] = Relationship(back_populates="laboratorios", secondary=UsuarioLaboratorioAssociation)