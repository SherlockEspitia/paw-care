from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List, Optional

from app.db.connection import get_db
from app.repository.historial_servicio import HistorialServicioRepository
from app.services.historial_servicio import HistorialServicioService
from app.schemas.historial_servicio import HistorialServicioCreate, HistorialServicioResponse, HistorialServicioUpdate, HistorialServicioWithServicio

router = APIRouter(
    prefix="/api/v1/historial-servicios",
    tags=["historial-servicios"],
    responses={404: {"description": "No encontrado"}},
)

def get_historial_servicio_repository(db: Session = Depends(get_db)) -> HistorialServicioRepository:
    return HistorialServicioRepository(db)

def get_historial_servicio_service(repository: HistorialServicioRepository = Depends(get_historial_servicio_repository)) -> HistorialServicioService:
    return HistorialServicioService(repository)

@router.get("/", response_model=List[HistorialServicioResponse], summary="Listar historiales de servicio")
async def list_historiales_servicio(
    skip: int = Query(0, ge=0, description="Número de registros a saltar"),
    limit: int = Query(10, ge=1, le=100, description="Número máximo de registros a devolver"),
    service: HistorialServicioService = Depends(get_historial_servicio_service)
):
    return service.get_all(skip, limit)

@router.post("/", response_model=HistorialServicioResponse, status_code=status.HTTP_201_CREATED, summary="Crear historial de servicio")
async def create_historial_servicio(
    historial: HistorialServicioCreate,
    service: HistorialServicioService = Depends(get_historial_servicio_service)
):
    return service.create(historial)

@router.get("/{historial_id}", response_model=HistorialServicioResponse, summary="Obtener historial de servicio")
async def get_historial_servicio(
    historial_id: int,
    service: HistorialServicioService = Depends(get_historial_servicio_service)
):
    return service.get_by_id(historial_id)

@router.get("/{historial_id}/detailed", response_model=HistorialServicioWithServicio, summary="Obtener historial con servicio")
async def get_historial_servicio_detailed(
    historial_id: int,
    service: HistorialServicioService = Depends(get_historial_servicio_service)
):
    return service.get_with_servicio(historial_id)

@router.put("/{historial_id}", response_model=HistorialServicioResponse, summary="Actualizar historial de servicio")
async def update_historial_servicio(
    historial_id: int,
    historial: HistorialServicioUpdate,
    service: HistorialServicioService = Depends(get_historial_servicio_service)
):
    return service.update(historial_id, historial)

@router.delete("/{historial_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Eliminar historial de servicio")
async def delete_historial_servicio(
    historial_id: int,
    service: HistorialServicioService = Depends(get_historial_servicio_service)
):
    service.delete(historial_id)
    return None

@router.get("/servicio/{servicio_id}", response_model=List[HistorialServicioResponse], summary="Obtener historiales por servicio")
async def get_historiales_by_servicio(
    servicio_id: int,
    service: HistorialServicioService = Depends(get_historial_servicio_service)
):
    return service.get_by_servicio(servicio_id)

@router.get("/estado/{estado}", response_model=List[HistorialServicioResponse], summary="Obtener historiales por estado")
async def get_historiales_by_estado(
    estado: str,
    service: HistorialServicioService = Depends(get_historial_servicio_service)
):
    return service.get_by_estado(estado)

@router.get("/fecha/rango", response_model=List[HistorialServicioResponse], summary="Obtener historiales por rango de fechas")
async def get_historiales_by_fecha_rango(
    fecha_inicio: datetime = Query(..., description="Fecha de inicio del rango"),
    fecha_fin: datetime = Query(..., description="Fecha de fin del rango"),
    service: HistorialServicioService = Depends(get_historial_servicio_service)
):
    return service.get_by_fecha_rango(fecha_inicio, fecha_fin)

@router.post("/servicio/{servicio_id}/iniciar", response_model=HistorialServicioResponse, summary="Iniciar un servicio")
async def iniciar_servicio(
    servicio_id: int,
    notas: Optional[str] = Query(None, description="Notas adicionales"),
    service: HistorialServicioService = Depends(get_historial_servicio_service)
):
    return service.iniciar_servicio(servicio_id, notas)

@router.post("/servicio/{servicio_id}/finalizar", response_model=HistorialServicioResponse, summary="Finalizar un servicio")
async def finalizar_servicio(
    servicio_id: int,
    estado: str = Query(..., description="Estado final: completado o cancelado"),
    notas: Optional[str] = Query(None, description="Notas adicionales"),
    service: HistorialServicioService = Depends(get_historial_servicio_service)
):
    return service.finalizar_servicio(servicio_id, estado, notas)