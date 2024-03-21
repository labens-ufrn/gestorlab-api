import uuid
from datetime import datetime
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship
from core.config import settings
from sqlalchemy.dialects.postgresql import UUID

class Laboratorio(settings.DBBaseModel):
    __tablename__ = 'laboratorios'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    coordenador_id = Column(UUID(as_uuid=True), ForeignKey("usuario.id"), nullable=False)
    nome = Column(String(256), nullable=False)
    descricao = Column(String(5000), nullable=True)
    email = Column(String(256), nullable=True)
    data_inicial = Column(String(256), default=lambda: datetime.now().strftime('%Y-%m-%d %H:%M:%S'), nullable=False)
    data_up = Column(String(256), default=lambda: datetime.now().strftime('%Y-%m-%d %H:%M:%S'), nullable=False)
    coordenador = relationship("Usuario", back_populates='laboratorios', lazy='joined')