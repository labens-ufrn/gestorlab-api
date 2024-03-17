import uuid
from datetime import datetime
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from core.config import settings

class Laboratorio(settings.DBBaseModel):
    __tablename__='laboratorios'
    id = Column(
        autoincrement=True,
        default_factory=uuid.uuid4,
        primary_key=True,
        nullable=False
    )
    coordenador_id = Column(String, foreign_key="usuario.id", nullable=False)
    nome = Column(String(256), nullable=False)
    descricao = Column(String(5000), nullable=True)
    email = Column(String(256), nullable=True)
    data_inicial = Column(default=datetime.now, nullable=False)
    data_up = Column(default=datetime.now, nullable=False)
    coordenador = relationship("Usuario", back_populates='laboratorios', lazy='joined')