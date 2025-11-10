from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.db.connection import get_db
from app.repository.mascota import MascotaRepository
from app.services.mascota import MascotaService
from app.schemas.mascota import MascotaCreate, MascotaResponse, MascotaUpdate, MascotaWithPropietario

router = APIRouter(
    prefix="/mascotas",
    tags=["Mascotas"],
    responses={404:{"description": "No encontrado"}}
)

def get_mascota_repository(session:Session = Depends(get_db))->MascotaRepository:
    return MascotaRepository(session)

def get_mascota_service(repository:MascotaRepository= Depends(get_mascota_repository))-> MascotaService:
    return MascotaService(repository)

@router.get("/", response_model=List[MascotaResponse], summary="Listar mascota")
async def list_mascota(
    skip:int = Query(0, ge=0, description="Numero de resgistros a saltar"),
    limit:int = Query(10, ge=1, le=100, description="Numero  maximo de resgistros a devolver"),
    service: MascotaService = Depends(get_mascota_service)
):
    return service.get_all(skip, limit)

@router.post("/", response_model=MascotaResponse, status_code=status.HTTP_201_CREATED, summary="Crear Mascota")
async def create_mascota(mascota:MascotaCreate, service: MascotaService= Depends(get_mascota_service)):
    return service.create(mascota)

@router.get("/{mascota_id}", response_model=MascotaWithPropietario, summary="Obtener mascota")
async def get_mascota(mascota_id:int, service:MascotaService = Depends(get_mascota_service)):
    return service.get_by_id(mascota_id)

@router.put("/{mascota_id}", response_model=MascotaResponse, summary="Actualizar mascota")
async def update_mascota( mascota_id:int, mascota_data:MascotaUpdate, service:MascotaService = Depends(get_mascota_service)):
    return service.update(mascota_id, mascota_data)

@router.delete("/{mascota_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Eliminar mascota")
async def delete_mascota(mascota_id:int, service: MascotaService = Depends(get_mascota_service)):    
    service.delete(mascota_id)
    return None

@router.get("/propietario/{propietario_id}", response_model=List[MascotaResponse], summary ="Obtener mascotas por propietario")
async def get_mascotas_by_propietario(propietario_id:int, service:MascotaService = Depends(get_mascota_service)):
    return service.get_by_propietario(propietario_id)