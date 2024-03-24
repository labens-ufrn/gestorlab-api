import uuid
from datetime import datetime
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship
from core.config import settings
from sqlalchemy.dialects.postgresql import UUID
from models.associetions import usuario_projeto_association
class Projeto(settings.DBBaseModel):
    __tablename__ = 'projetos'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    titulo = Column(String(256), unique=True, nullable=False)
    descricao = Column(String(5000), nullable=True)
    autor_id = Column(UUID(as_uuid=True), ForeignKey("usuario.id"), nullable=False)
    data_inicial = Column(String(256), default=lambda: datetime.now().strftime('%Y-%m-%d %H:%M:%S'), nullable=False)
    data_up = Column(String(256), default=lambda: datetime.now().strftime('%Y-%m-%d %H:%M:%S'), nullable=False)
    autor = relationship("Usuario", back_populates='projetos', lazy='joined')
    membros = relationship(
        "Usuario",
        secondary=usuario_projeto_association,
        back_populates="projetos",
        lazy="joined"
    )