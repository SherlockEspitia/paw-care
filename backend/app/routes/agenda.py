from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from datetime import date, time
from typing import List, Optional

from app.db.connection import get_db
from app.repository.agenda import AgendaRepository
from app.services.agenda import AgendaService
from app.schemas.agenda import AgendaCreate, AgendaResponse, AgendaUpdate, AgendaWithServicio

router = APIRouter(
    prefix="/api/v1/agendas",
    tags=["Agendas"],
    responses={404: {"description": "No encontrado"}},
)

def get_agenda_repository(db: Session = Depends(get_db)) -> AgendaRepository:
    return AgendaRepository(db)

def get_agenda_service(repository: AgendaRepository = Depends(get_agenda_repository)) -> AgendaService:
    return AgendaService(repository)

@router.get("/", response_model=List[AgendaResponse], summary="Listar agendas")
async def list_agendas(
    skip: int = Query(0, ge=0, description="Número de registros a saltar"),
    limit: int = Query(10, ge=1, le=100, description="Número máximo de registros a devolver"),
    service: AgendaService = Depends(get_agenda_service)
):
    return service.get_all(skip, limit)

@router.post("/", response_model=AgendaResponse, status_code=status.HTTP_201_CREATED, summary="Crear agenda")
async def create_agenda(
    agenda: AgendaCreate,
    service: AgendaService = Depends(get_agenda_service)
):
    return service.create(agenda)

@router.get("/{agenda_id}", response_model=AgendaResponse, summary="Obtener agenda")
async def get_agenda(
    agenda_id: int,
    service: AgendaService = Depends(get_agenda_service)
):
    return service.get_by_id(agenda_id)

@router.get("/{agenda_id}/detailed", response_model=AgendaWithServicio, summary="Obtener agenda con servicio")
async def get_agenda_detailed(
    agenda_id: int,
    service: AgendaService = Depends(get_agenda_service)
):
    return service.get_with_servicio(agenda_id)

@router.put("/{agenda_id}", response_model=AgendaResponse, summary="Actualizar agenda")
async def update_agenda(
    agenda_id: int,
    agenda: AgendaUpdate,
    service: AgendaService = Depends(get_agenda_service)
):
    return service.update(agenda_id, agenda)

@router.delete("/{agenda_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Eliminar agenda")
async def delete_agenda(
    agenda_id: int,
    service: AgendaService = Depends(get_agenda_service)
):
    service.delete(agenda_id)
    return None

@router.get("/servicio/{servicio_id}", response_model=List[AgendaResponse], summary="Obtener agendas por servicio")
async def get_agendas_by_servicio(
    servicio_id: int,
    service: AgendaService = Depends(get_agenda_service)
):
    return service.get_by_servicio(servicio_id)

@router.get("/fecha/{fecha}", response_model=List[AgendaResponse], summary="Obtener agendas por fecha")
async def get_agendas_by_fecha(
    fecha: date,
    service: AgendaService = Depends(get_agenda_service)
):
    return service.get_by_fecha(fecha)

@router.get("/disponibilidad/verificar", summary="Verificar disponibilidad de horario")
async def verificar_disponibilidad(
    fecha: date = Query(..., description="Fecha a verificar"),
    hora_inicio: time = Query(..., description="Hora de inicio"),
    hora_fin: time = Query(..., description="Hora de fin"),
    service: AgendaService = Depends(get_agenda_service)
):
    disponible = service.get_disponibilidad(fecha, hora_inicio, hora_fin)
    return {
        "disponible": disponible,
        "fecha": fecha,
        "hora_inicio": hora_inicio,
        "hora_fin": hora_fin
    }