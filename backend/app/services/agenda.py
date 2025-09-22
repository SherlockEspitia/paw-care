from typing import List, Optional
from datetime import date, time
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repository.agenda import AgendaRepository
from app.schemas.agenda import AgendaCreate, AgendaUpdate, AgendaResponse, AgendaWithServicio
from app.models.agenda import Agenda

class AgendaService:
    def __init__(self, repository: AgendaRepository):
        self.repository = repository
    
    def get_all(self, skip: int = 0, limit: int = 10) -> List[AgendaResponse]:
        return self.repository.get_all(skip, limit)
    
    def get_by_id(self, agenda_id: int) -> Optional[AgendaResponse]:
        agenda = self.repository.get_by_id(agenda_id)
        if not agenda:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Agenda no encontrada"
            )
        return agenda
    
    def get_with_servicio(self, agenda_id: int) -> Optional[AgendaWithServicio]:
        agenda = self.repository.get_with_servicio(agenda_id)
        if not agenda:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Agenda no encontrada"
            )
        return agenda
    
    def create(self, agenda_data: AgendaCreate) -> AgendaResponse:
        # Verificar si el servicio existe
        from repositories.servicio_repository import ServicioRepository
        servicio_repo = ServicioRepository(self.repository.session)
        servicio = servicio_repo.get_by_id(agenda_data.IDservicio)
        
        if not servicio:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Servicio no encontrado"
            )
        
        # Verificar conflictos de horario
        if agenda_data.fecha and agenda_data.hora_inicio and agenda_data.hora_fin:
            conflictos = self.repository.get_conflictos_horarios(
                agenda_data.fecha, 
                agenda_data.hora_inicio, 
                agenda_data.hora_fin
            )
            
            if conflictos:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Existe un conflicto de horario con otra agenda"
                )
        
        return self.repository.create(agenda_data)
    
    def update(self, agenda_id: int, agenda_data: AgendaUpdate) -> Optional[AgendaResponse]:
        agenda = self.repository.get_by_id(agenda_id)
        if not agenda:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Agenda no encontrada"
            )
        
        # Si se está actualizando el servicio, verificar que existe
        if agenda_data.IDservicio:
            from repositories.servicio_repository import ServicioRepository
            servicio_repo = ServicioRepository(self.repository.session)
            servicio = servicio_repo.get_by_id(agenda_data.IDservicio)
            
            if not servicio:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Servicio no encontrado"
                )
        
        # Verificar conflictos de horario si se actualizan fecha/hora
        fecha = agenda_data.fecha if agenda_data.fecha else agenda.fecha
        hora_inicio = agenda_data.hora_inicio if agenda_data.hora_inicio else agenda.hora_inicio
        hora_fin = agenda_data.hora_fin if agenda_data.hora_fin else agenda.hora_fin
        
        if fecha and hora_inicio and hora_fin:
            conflictos = self.repository.get_conflictos_horarios(
                fecha, hora_inicio, hora_fin, agenda_id
            )
            
            if conflictos:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Existe un conflicto de horario con otra agenda"
                )
        
        return self.repository.update(agenda_id, agenda_data)
    
    def delete(self, agenda_id: int) -> bool:
        agenda = self.repository.get_by_id(agenda_id)
        if not agenda:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Agenda no encontrada"
            )
        return self.repository.delete(agenda_id)
    
    def get_by_servicio(self, servicio_id: int) -> List[AgendaResponse]:
        from repositories.servicio_repository import ServicioRepository
        servicio_repo = ServicioRepository(self.repository.session)
        servicio = servicio_repo.get_by_id(servicio_id)
        
        if not servicio:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Servicio no encontrado"
            )
        
        return self.repository.get_by_servicio(servicio_id)
    
    def get_by_fecha(self, fecha: date) -> List[AgendaResponse]:
        return self.repository.get_by_fecha(fecha)
    
    def get_disponibilidad(self, fecha: date, hora_inicio: time, hora_fin: time) -> bool:
        """
        Verifica si un horario está disponible
        """
        conflictos = self.repository.get_conflictos_horarios(fecha, hora_inicio, hora_fin)
        return len(conflictos) == 0