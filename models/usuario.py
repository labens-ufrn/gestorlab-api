import uuid
from datetime import datetime
from sqlalchemy import BigInteger, String, Column
from sqlalchemy.orm import relationship
from core.config import settings
from sqlalchemy.dialects.postgresql import UUID
from models.associetions import usuario_laboratorio_association, usuario_projeto_association
class Usuario(settings.DBBaseModel):
    __tablename__ = 'usuario'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    primeiro_nome = Column(String(256), nullable=False)
    segundo_nome = Column(String(256), nullable=False)
    matricula = Column(BigInteger, nullable=False, unique=True)
    email = Column(String(256), index=True, nullable=False, unique=True)
    tel = Column(BigInteger, nullable=True)
    senha = Column(String(256), nullable=False)
    laboratorios = relationship(
        "Laboratorio",
        secondary=usuario_laboratorio_association,
        back_populates="membros",
        lazy="joined"
    )
    projetos = relationship(
        "Projeto",
        secondary=usuario_projeto_association,
        back_populates="membros",
        lazy="joined"
    )
    data_inicial = Column(String(256), default=lambda: datetime.now().strftime('%Y-%m-%d %H:%M:%S'), nullable=False)
    data_atualizacao = Column(String(256), default=lambda: datetime.now().strftime('%Y-%m-%d %H:%M:%S'), nullable=False)
    tag = Column(BigInteger, default=1, nullable=False)