from fastapi import APIRouter, Depends, Query, Path, status
from sqlalchemy.orm import Session
from typing import List, Optional
from db.connection import get_db
from schemas.propietario import (PropietarioCreate, PropietarioList, PropietarioResponse, PropietarioSummary, PropietarioUpdate)
from services.propietario import PropietarioService
from schemas.response_models import PaginatedResponse

router = APIRouter(
    prefix="/propietarios",
    tags = ["Propietarios"],
    responses={404:{"description": "No encontrado"}}
)

@router.get("/", response_model=PropietarioList, summary="Listar propietarios", description="Obtener lista paginada de propietarios registrados")
async def get_propietarios( page: int = Query(default=1, ge=1, description="Número de Pagina"), 
    per_page:int = Query(default=10, ge=1, le=100, description="Elementos por pagina"), session:Session=Depends(get_db)):
    service = PropietarioService(session)
    return service.get_propietario_paginated(page=page, per_page=per_page)

@router.get("/{propietario_id}", response_model=PropietarioResponse, summary="Obtener propietario", description="Obtener informacion detallada de un propietario por su ID")
async def get_propietario(propietario_id:int=Path(..., description="ID del Propietario", gt=0), session:Session= Depends(get_db)):
    service = PropietarioService(session)
    return service.get_propietario_by_id(propietario_id)

@router.post("/", response_model=PropietarioResponse, status_code=status.HTTP_201_CREATED, summary="Crear propietario", description="Registrar un nuevo propietario en el sistema")
async def create_propietario(propietario_data:PropietarioCreate, session:Session = Depends(get_db)):
    service = PropietarioService(session)
    return service.create_propietario(propietario_data)

@router.put("/{propietario_id}", response_model=PropietarioResponse, summary="Actualizar propietario", description="Actualizar informacion de un propietario existente")
async def update_propietario(propietario_id:int = Path(..., description="ID del propietario", gt=0), propietario_data: PropietarioUpdate= ..., session:Session= Depends(get_db)):
    service = PropietarioService(session)
    return service.update_propietario(propietario_id, propietario_data)

@router.delete("/{propietario_id}", summary="Eliminar propietario", description="Eliminar un propietario del sistema")
async def delete_propietario( propietario_id:int = Path(..., description="ID del propietario", gt=0), session:Session= Depends(get_db)):
    service = PropietarioService(session)
    return service.delete_propietario(propietario_id)

@router.get('/search/by-name', response_model=List[PropietarioSummary], summary="Buscar propietarios", description="Buscar propietarios por nombre o apellido")
async def search_propietarios(q:str= Query(..., description="Termino de busqueda", min_length=2), session:Session = Depends(get_db)):
    service = PropietarioService(session)
    return service.search_propietarios(q)

@router.get('/filter/by-city', response_model=List[PropietarioResponse], summary="Filtrar por ciudad", description="Obtener propietarios de una ciudad especifica")
async def get_propietarios_by_city(ciudad:str = Query(..., description="Nombre de la ciudad"),session:Session = Depends(get_db)):
    service = PropietarioService(session)
    return service.get_propietario_by_city(ciudad)
