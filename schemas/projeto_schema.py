from typing import Optional, List
from pydantic import BaseModel, UUID4
from datetime import datetime

class ProjetoSchema(BaseModel):
    id: Optional[UUID4] = None 
    titulo: str
    descricao: str
    autor_id: Optional[UUID4] = None 
    data_inicial: datetime
    data_up: datetime
    lista_membros: Optional[List[str]] = None

    class Config:
        from_attributes = True