import uuid
from datetime import datetime
from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship

class Usuario(SQLModel, table=True):
    __tablename__: str = 'usuario'

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False
    )
    first_name: str = Field(nullable=False)
    second_name: str = Field(nullable=False)
    registration: int = Field(nullable=False)
    email: str = Field(nullable=False)
    tel: Optional[int] = Field(nullable=True)
    # Definindo a relação com Laboratorio
    laboratorios: List["LaboratorioUsuarioAssociation"] = Relationship(back_populates="usuario")
    # Definindo a relação com Projeto
    projetos: List["ProjetoUsuarioAssociation"] = Relationship(back_populates="usuario")

    data_inicial: Optional[datetime] = Field(default=datetime.now, nullable=False)
    data_up: Optional[datetime] = Field(default=datetime.now, nullable=False)
    tag: int = Field(default=2, nullable=False)