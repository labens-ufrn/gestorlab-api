from sqlalchemy import Column, ForeignKey, Table
from core.config import settings
from sqlalchemy.dialects.postgresql import UUID

# Tabela de associação muitos para muitos entre Usuario e Laboratorio
usuario_laboratorio_association = Table(
    'usuario_laboratorio',
    settings.DBBaseModel.metadata,
    Column('usuario_id', UUID(as_uuid=True), ForeignKey('usuario.id')),
    Column('laboratorio_id', UUID(as_uuid=True), ForeignKey('laboratorios.id'))
)

# Tabela de associação muitos para muitos entre Usuario e Projeto
usuario_projeto_association = Table(
    'usuario_projeto',
    settings.DBBaseModel.metadata,
    Column('usuario_id', UUID(as_uuid=True), ForeignKey('usuario.id')),
    Column('projeto_id', UUID(as_uuid=True), ForeignKey('projetos.id'))
)