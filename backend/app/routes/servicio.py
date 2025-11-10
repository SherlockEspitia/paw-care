from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.connection import get_db
from app.repository.servicio import ServicioRepository
from app.services.servicio import ServicioService
from app.schemas.servicio import ServicioCreate, ServicioResponse, ServicioUpdate, ServicioDetailed

router = APIRouter(
    prefix="/api/v1/servicios",
    tags=["Servicios"],
    responses={404: {"description": "No encontrado"}},
)

def get_servicio_repository(db: Session = Depends(get_db)) -> ServicioRepository:
    return ServicioRepository(db)

def get_servicio_service(repository: ServicioRepository = Depends(get_servicio_repository)) -> ServicioService:
    return ServicioService(repository)

@router.get("/", response_model=List[ServicioResponse], summary="Listar servicios")
async def list_servicios(
    skip: int = Query(0, ge=0, description="Número de registros a saltar"),
    limit: int = Query(10, ge=1, le=100, description="Número máximo de registros a devolver"),
    service: ServicioService = Depends(get_servicio_service)
):
    return service.get_all(skip, limit)

@router.post("/", response_model=ServicioResponse, status_code=status.HTTP_201_CREATED, summary="Crear servicio")
async def create_servicio(
    servicio: ServicioCreate,
    service: ServicioService = Depends(get_servicio_service)
):
    return service.create(servicio)

@router.get("/{servicio_id}", response_model=ServicioResponse, summary="Obtener servicio")
async def get_servicio(
    servicio_id: int,
    service: ServicioService = Depends(get_servicio_service)
):
    return service.get_by_id(servicio_id)

@router.get("/{servicio_id}/detailed", response_model=ServicioDetailed, summary="Obtener servicio con detalles completos")
async def get_servicio_detailed(
    servicio_id: int,
    service: ServicioService = Depends(get_servicio_service)
):
    return service.get_detailed_by_id(servicio_id)

@router.put("/{servicio_id}", response_model=ServicioResponse, summary="Actualizar servicio")
async def update_servicio(
    servicio_id: int,
    servicio: ServicioUpdate,
    service: ServicioService = Depends(get_servicio_service)
):
    return service.update(servicio_id, servicio)

@router.delete("/{servicio_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Eliminar servicio")
async def delete_servicio(
    servicio_id: int,
    service: ServicioService = Depends(get_servicio_service)
):
    service.delete(servicio_id)
    return None

@router.get("/cuidador/{cuidador_id}", response_model=List[ServicioResponse], summary="Obtener servicios por cuidador")
async def get_servicios_by_cuidador(
    cuidador_id: int,
    service: ServicioService = Depends(get_servicio_service)
):
    return service.get_by_cuidador(cuidador_id)

@router.get("/mascota/{mascota_id}", response_model=List[ServicioResponse], summary="Obtener servicios por mascota")
async def get_servicios_by_mascota(
    mascota_id: int,
    service: ServicioService = Depends(get_servicio_service)
):
    return service.get_by_mascota(mascota_id)

@router.get("/propietario/{propietario_id}", response_model=List[ServicioResponse], summary="Obtener servicios por propietario")
async def get_servicios_by_propietario(
    propietario_id: int,
    service: ServicioService = Depends(get_servicio_service)
):
    return service.get_by_propietario(propietario_id)