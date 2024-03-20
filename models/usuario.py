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
    primeiro_nome = Column(String(256),nullable=False)
    segundo_nome= Column(String(256),nullable=False)
    matricula= Column(Integer, nullable=False, unique=True)
    email = Column(String(256),index=True, nullable=False)
    tel = Column(Integer(11),nullable=True)
    senha = Column(String(256), nullable=False)
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
    data_atualizacao = Column(default=datetime.now, nullable=False)
    tag = Column(Integer(1),default=1, nullable=False)