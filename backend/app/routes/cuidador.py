from fastapi import APIRouter, Depends, Query, Path, status
from sqlalchemy.orm import Session
from typing import List, Optional
from db.connection import get_db
from schemas.cuidador import CuidadorCreate, CuidadorResponse, CuidadorUpdate
from services.cuidador import CuidadorService
from schemas.response_models import PaginatedResponse

router = APIRouter(
    prefix='/cuidadores',
    tags= ['Cuidadores'],
    responses = {404, {"description":"No encontrado"}}
)

@router.get("/{cuidador_id}", response_model=CuidadorResponse, summary="Obtener cuidador", description="Obtener informacion detallada de un propietario por su ID")
async def get_cuidador(cuidador_id:int= Path(..., description="ID del Cuidador", gt=0), session:Session= Depends(get_db)):
    service = CuidadorService(session)
    return service.get_cuidador_by_id(cuidador_id)

@router.post("/", response_model= CuidadorResponse, status_code = status.HTTP_201_CREATED, summary="Crear Cuidador", description="Registrar un nuevo cuidador en el sistema")
async def create_cuidador(cuidador_data:CuidadorCreate, session:Session = Depends(get_db)):
    service = CuidadorService(session)
    return service.create_cuidador(cuidador_data)

@router.put("/{cuidador_id}", response_model= PropietarioResponse, status_code=status.HTTP_201_CREATED, summary="Actualizar informacion de un cuidador existente")
async def update_cuidador(cuidador_id:int=Path(..., description="ID del Cuidador", gt=0), cuidador_data:CuidadorUpdate=..., session:Session=Depends(get_db)):
    service = CuidadorService(session)
    return service.update_cuidador(cuidador_id, cuidador_data)

@router.delete("/{propietario_id}", response_model=PropietarioResponse, summary="Eliminar un cuidador del sistema")
async def delete_cuidador(cuidador_id:int=Path(..., description="ID del cuidador", gt=0), session:Session = Depends(get_db)):
    service = CuidadorService(session)
    return service.delete_cuidador(cuidador_id)


