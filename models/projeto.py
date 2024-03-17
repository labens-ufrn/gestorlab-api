import uuid
from datetime import datetime
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from core.config import settings

class Projeto(settings.DBBaseModel):
    __tablename__='projetos'
    id = Column(
        autoincrement=True,
        default_factory=uuid.uuid4,
        primary_key=True,
        nullable=False
    )
    titulo = Column(String(), nullable=False)
    descricao= Column(String(), nullable=True)
    autor_id= Column(String,foreign_key="usuario.id", nullable=False)
    data_inicial= Column(default=datetime.now, nullable=False)
    data_up= Column(default=datetime.now, nullable=False)
    autor = relationship("Usuario", back_populates='projetos', lazy='joined')