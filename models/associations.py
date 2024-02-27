from sqlmodel import SQLModel, Field
import uuid

class UsuarioLaboratorioAssociation(SQLModel, table=True):
    id: uuid.UUID = Field(
        default_factory= uuid.uuid4, 
        primary_key=True,
        nullable=False
    )
    usuario_id: uuid.UUID = Field(foreign_key="usuario.id") 
    laboratorio_id: uuid.UUID = Field(foreign_key="laboratorio.id")

class UsuarioProjetoAssociation(SQLModel, table=True):
    id: uuid.UUID = Field(
        default_factory= uuid.uuid4, 
        primary_key=True,
        nullable=False
    )
    usuario_id: uuid.UUID = Field(foreign_key="usuario.id") 
    projeto_id: uuid.UUID = Field(foreign_key="projeto.id")

class LaboratorioProjetoAssociation(SQLModel, table=True):
    id: uuid.UUID = Field(
        default_factory= uuid.uuid4, 
        primary_key=True,
        nullable=False
    )
    laboratorio_id: uuid.UUID = Field(foreign_key="laboratorio.id") 
    projeto_id: uuid.UUID = Field(foreign_key="projeto.id")