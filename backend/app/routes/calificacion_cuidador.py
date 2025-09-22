from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional, Dict, Any

from app.db.connection import get_db
from repository.calificacion_cuidador import CalificacionCuidadorRepository
from app.services.calificacion_cuidador import CalificacionCuidadorService
from app.schemas.calificacion_cuidador import CalificacionCuidadorCreate, CalificacionCuidadorResponse, CalificacionCuidadorUpdate, CalificacionCuidadorDetailed

router = APIRouter(
    prefix="/api/v1/calificaciones-cuidadores",
    tags=["calificaciones-cuidadores"],
    responses={404: {"description": "No encontrado"}},
)

def get_calificacion_cuidador_repository(db: Session = Depends(get_db)) -> CalificacionCuidadorRepository:
    return CalificacionCuidadorRepository(db)

def get_calificacion_cuidador_service(repository: CalificacionCuidadorRepository = Depends(get_calificacion_cuidador_repository)) -> CalificacionCuidadorService:
    return CalificacionCuidadorService(repository)

@router.get("/", response_model=List[CalificacionCuidadorResponse], summary="Listar calificaciones de cuidadores")
async def list_calificaciones(
    skip: int = Query(0, ge=0, description="Número de registros a saltar"),
    limit: int = Query(10, ge=1, le=100, description="Número máximo de registros a devolver"),
    service: CalificacionCuidadorService = Depends(get_calificacion_cuidador_service)
):
    return service.get_all(skip, limit)

@router.post("/", response_model=CalificacionCuidadorResponse, status_code=status.HTTP_201_CREATED, summary="Crear calificación de cuidador")
async def create_calificacion(
    calificacion: CalificacionCuidadorCreate,
    service: CalificacionCuidadorService = Depends(get_calificacion_cuidador_service)
):
    return service.create(calificacion)

@router.get("/{calificacion_id}", response_model=CalificacionCuidadorResponse, summary="Obtener calificación")
async def get_calificacion(
    calificacion_id: int,
    service: CalificacionCuidadorService = Depends(get_calificacion_cuidador_service)
):
    return service.get_by_id(calificacion_id)

@router.get("/{calificacion_id}/detailed", response_model=CalificacionCuidadorDetailed, summary="Obtener calificación con detalles completos")
async def get_calificacion_detailed(
    calificacion_id: int,
    service: CalificacionCuidadorService = Depends(get_calificacion_cuidador_service)
):
    return service.get_detailed_by_id(calificacion_id)

@router.put("/{calificacion_id}", response_model=CalificacionCuidadorResponse, summary="Actualizar calificación")
async def update_calificacion(
    calificacion_id: int,
    calificacion: CalificacionCuidadorUpdate,
    service: CalificacionCuidadorService = Depends(get_calificacion_cuidador_service)
):
    return service.update(calificacion_id, calificacion)

@router.delete("/{calificacion_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Eliminar calificación")
async def delete_calificacion(
    calificacion_id: int,
    service: CalificacionCuidadorService = Depends(get_calificacion_cuidador_service)
):
    service.delete(calificacion_id)
    return None

@router.get("/cuidador/{cuidador_id}", response_model=List[CalificacionCuidadorResponse], summary="Obtener calificaciones por cuidador")
async def get_calificaciones_by_cuidador(
    cuidador_id: int,
    service: CalificacionCuidadorService = Depends(get_calificacion_cuidador_service)
):
    return service.get_by_cuidador(cuidador_id)

@router.get("/propietario/{propietario_id}", response_model=List[CalificacionCuidadorResponse], summary="Obtener calificaciones por propietario")
async def get_calificaciones_by_propietario(
    propietario_id: int,
    service: CalificacionCuidadorService = Depends(get_calificacion_cuidador_service)
):
    return service.get_by_propietario(propietario_id)

@router.get("/servicio/{servicio_id}", response_model=List[CalificacionCuidadorResponse], summary="Obtener calificaciones por servicio")
async def get_calificaciones_by_servicio(
    servicio_id: int,
    service: CalificacionCuidadorService = Depends(get_calificacion_cuidador_service)
):
    return service.get_by_servicio(servicio_id)

@router.get("/cuidador/{cuidador_id}/promedio", summary="Obtener promedio de calificaciones de un cuidador")
async def get_promedio_cuidador(
    cuidador_id: int,
    service: CalificacionCuidadorService = Depends(get_calificacion_cuidador_service)
) -> Dict[str, Any]:
    return service.get_promedio_cuidador(cuidador_id)

@router.get("/cuidador/{cuidador_id}/estadisticas", summary="Obtener estadísticas detalladas de calificaciones de un cuidador")
async def get_estadisticas_cuidador(
    cuidador_id: int,
    service: CalificacionCuidadorService = Depends(get_calificacion_cuidador_service)
) -> Dict[str, Any]:
    return service.get_estadisticas_cuidador(cuidador_id)