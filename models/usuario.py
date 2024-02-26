 
import uuid
from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel

class Usuarios(SQLModel,table=True):
    __tablename__: str = 'usuarios'

    id: uuid.UUID = Field(
        default_factory= uuid.uuid4, 
        primary_key=True,
        index=True,
        nullable=False
    )
    first_name: str = Field(nullable=False)
    second_name: str = Field(nullable=False)
    registration: int = Field(nullable=False)
    email: str = Field(nullable=False)
    tel: Optional[int] = Field(nullable=True)
    data_inicial: datetime = Field(default=datetime.now, nullable=False)
    data_att: datetime = Field(default=datetime.now, nullable=False)
    tag: int = Field(default=2, nullable=False)