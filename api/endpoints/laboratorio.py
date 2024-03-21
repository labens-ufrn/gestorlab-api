from typing import List

from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import  AsyncSession
from sqlalchemy.future import  select

from models.laboratorio import Laboratorio
from models.usuario import Usuario
from schemas.laboratorio_schema import LaboratorioSchema, LaboratorioSchemaCreate
from core.deps import get_session, get_current_user

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

    for id in laboratorio.lista_membros:
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
async def get_laboratorio(laboratorio_id: int, db: AsyncSession = Depends(get_session)):
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
async def put_laboratorio(laboratorio_id: int, laboratorio: LaboratorioSchema, db: AsyncSession = Depends(get_session), usuario_logado: Usuario = Depends(get_current_user)):
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
            if usuario_logado.id != laboratorio_up.id:
                laboratorio_up.usuario_id = usuario_logado.id

            await session.commit()
            
            return laboratorio_up
        
        else:
            raise HTTPException(detail="laboratorio não encontrado!", status_code=status.HTTP_404_NOT_FOUND)
        
#DELETE laboratorio
@router.delete('/{laboratorio_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_laboratorio(laboratorio_id: int, db: AsyncSession = Depends(get_session), usuario_logado: Usuario = Depends(get_current_user)):
    async with db as session:
        query = select(Laboratorio).filter(Laboratorio.id == laboratorio_id).filter(Laboratorio.usuario_id == usuario_logado.id)
        result = await session.execute(query)
        laboratorio_del: Laboratorio = result.scalars().unique().one_or_none()
    
        if laboratorio_del:
           
            await session.delete(laboratorio_del)
            await session.commit()
            
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        
        else:
            raise HTTPException(detail="laboratorio não encontrado!", status_code=status.HTTP_404_NOT_FOUND)