from typing import List

from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import  AsyncSession
from sqlalchemy.future import  select

from models.laboratorio import Laboratorio
from models.usuario import Usuario
from schemas.laboratorio_schema import LaboratorioSchema, LaboratorioSchemaCreate, LaboratorioSchemaUp
from core.deps import get_session, get_current_user
from datetime import datetime

router = APIRouter()

#POST Laboratorio
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=LaboratorioSchema)
async def post_laboratorio(
    laboratorio: LaboratorioSchemaCreate, 
    usuario_logado: Usuario = Depends(get_current_user), 
    db: AsyncSession = Depends(get_session)
):
    async with db as session:
        query = select(Usuario)
        result = await session.execute(query)
        usuarios: List[Usuario] = result.scalars().unique().all()

    membrosList: List[Usuario] = []

    for id in laboratorio.membros:
        # Verificar se o membro está na lista de usuários
        for usuario in usuarios:
            if id == usuario.id:
                membrosList.append(usuario)
    
    novo_laboratorio: Laboratorio = Laboratorio(
        coordenador_id= usuario_logado.id,
        nome = laboratorio.nome,
        descricao= laboratorio.descricao,
        email= laboratorio.email,
        membros = membrosList
    )

    db.add(novo_laboratorio)
    await db.commit()

    return novo_laboratorio

#GET Laboratorios
@router.get('/', response_model= List[LaboratorioSchema], status_code=status.HTTP_200_OK)
async def get_laboratorios(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(Laboratorio)
        result = await session.execute(query)
        laboratorios: List[Laboratorio] = result.scalars().unique().all()

    return laboratorios

#GET laboratorio
@router.get('/{laboratorio_id}', response_model= LaboratorioSchema, status_code=status.HTTP_200_OK)
async def get_laboratorio(laboratorio_id: str, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(Laboratorio).filter(Laboratorio.id == laboratorio_id)
        result = await session.execute(query)
        laboratorio: Laboratorio = result.scalars().unique().one_or_none()
    
    if laboratorio:
        return laboratorio
    else:
        raise HTTPException(detail="laboratorio não encontrado", status_code=status.HTTP_404_NOT_FOUND)

#PUT laboratorio
@router.put('/{laboratorio_id}', response_model=LaboratorioSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_laboratorio(laboratorio_id: str, laboratorio: LaboratorioSchemaUp, db: AsyncSession = Depends(get_session), usuario_logado: Usuario = Depends(get_current_user)):
    async with db as session:
        query = select(Laboratorio).filter(Laboratorio.id == laboratorio_id)
        result = await session.execute(query)
        laboratorio_up: Laboratorio = result.scalars().unique().one_or_none()
    
        if laboratorio_up:
            if laboratorio.nome:
                laboratorio_up.nome = laboratorio.nome
            if laboratorio.descricao:
                laboratorio_up.descricao = laboratorio.descricao
            if laboratorio.email:
                laboratorio_up.email= laboratorio.email
            if laboratorio.membros:
                # Filtrar usuários pelo ID fornecido no corpo da solicitação
                membrosList = [usuario for usuario in laboratorio.membros]
                # Adicionar usuários à lista de membros se eles não estiverem lá
                for usuario_id in membrosList:
                    if usuario_id not in [membro.id for membro in laboratorio_up.membros]:
                        usuario = await session.get(Usuario, usuario_id)
                        if usuario:
                            laboratorio_up.membros.append(usuario)
            else:
                # Se a lista de membros enviada estiver vazia, limpe a lista de membros do laboratório
                laboratorio_up.membros = []
           
            laboratorio_up.data_up = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            await session.commit()
            
            return laboratorio_up
        
        else:
            raise HTTPException(detail="laboratorio não encontrado!", status_code=status.HTTP_404_NOT_FOUND)
        
#DELETE laboratorio
@router.delete('/{laboratorio_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_laboratorio(laboratorio_id: str, db: AsyncSession = Depends(get_session), usuario_logado: Usuario = Depends(get_current_user)):
    async with db as session:
        query = select(Laboratorio).filter(Laboratorio.id == laboratorio_id).filter(Laboratorio.coordenador_id == usuario_logado.id)
        result = await session.execute(query)
        laboratorio_del: Laboratorio = result.scalars().unique().one_or_none()
    
        if laboratorio_del:
           
            await session.delete(laboratorio_del)
            await session.commit()
            
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        
        else:
            raise HTTPException(detail="Laboratorio não encontrado!", status_code=status.HTTP_404_NOT_FOUND)