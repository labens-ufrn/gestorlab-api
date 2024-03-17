import uuid
from datetime import datetime
from typing import Optional, List
from sqlalchemy import Integer, String, Column, Boolean
from sqlalchemy.orm import relationship
from core.config import settings

class Usuario(settings.DBBaseModel):
    __tablename__ = 'usuario'

    id = Column(
        autoincrement=True,
        default_factory=uuid.uuid4,
        primary_key=True,
        nullable=False
    )
    first_name = Column(String(256),nullable=False)
    second_name= Column(String(256),nullable=False)
    registration= Column(Integer, nullable=False)
    email = Column(String(256),index=True, nullable=False, unique=True)
    tel = Column(Integer(11),nullable=True)
    # Definindo a relação com Laboratorio
    laboratorios= relationship(
        "Laboratorio",
        back_populates="coordenador",
        lazy="joined"
    )
    # Definindo a relação com Projeto
    projetos = relationship(
        "Projeto",
        back_populates="autor",
        uselist=True,
        lazy="joined"
    )

    data_inicial = Column(default=datetime.now, nullable=False)
    data_up = Column(default=datetime.now, nullable=False)
    tag: int = Column(Integer(1),default=1, nullable=False)