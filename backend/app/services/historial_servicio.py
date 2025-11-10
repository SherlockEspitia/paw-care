from typing import List, Optional
from datetime import datetime
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repository.historial_servicio import HistorialServicioRepository
from app.schemas.historial_servicio import HistorialServicioCreate, HistorialServicioUpdate, HistorialServicioResponse, HistorialServicioWithServicio
from app.models.historial_servicio import HistorialServicio

class HistorialServicioService:
    def __init__(self, repository: HistorialServicioRepository):
        self.repository = repository
    
    def get_all(self, skip: int = 0, limit: int = 10) -> List[HistorialServicioResponse]:
        return self.repository.get_all(skip, limit)
    
    def get_by_id(self, historial_id: int) -> Optional[HistorialServicioResponse]:
        historial = self.repository.get_by_id(historial_id)
        if not historial:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Historial de servicio no encontrado"
            )
        return historial
    
    def get_with_servicio(self, historial_id: int) -> Optional[HistorialServicioWithServicio]:
        historial = self.repository.get_with_servicio(historial_id)
        if not historial:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Historial de servicio no encontrado"
            )
        return historial
    
    def create(self, historial_data: HistorialServicioCreate) -> HistorialServicioResponse:
        # Verificar si el servicio existe
        from repositories.servicio_repository import ServicioRepository
        servicio_repo = ServicioRepository(self.repository.session)
        servicio = servicio_repo.get_by_id(historial_data.IDservicio)
        
        if not servicio:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Servicio no encontrado"
            )
        
        # Verificar si ya existe un historial activo para este servicio
        if historial_data.estado == 'en_progreso':
            historial_activo = self.repository.get_historial_activo_servicio(historial_data.IDservicio)
            if historial_activo:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Ya existe un historial en progreso para este servicio"
                )
        
        # Si el estado es "completado" o "cancelado", debe tener fecha_fin
        if historial_data.estado in ['completado', 'cancelado'] and not historial_data.fecha_fin:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Los servicios completados o cancelados deben tener fecha de finalización"
            )
        
        return self.repository.create(historial_data)
    
    def update(self, historial_id: int, historial_data: HistorialServicioUpdate) -> Optional[HistorialServicioResponse]:
        historial = self.repository.get_by_id(historial_id)
        if not historial:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Historial de servicio no encontrado"
            )
        
        # Si se está actualizando el servicio, verificar que existe
        if historial_data.IDservicio:
            from repositories.servicio_repository import ServicioRepository
            servicio_repo = ServicioRepository(self.repository.session)
            servicio = servicio_repo.get_by_id(historial_data.IDservicio)
            
            if not servicio:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Servicio no encontrado"
                )
        
        # Validaciones de estado y fecha_fin
        estado = historial_data.estado if historial_data.estado else historial.estado
        
        if estado in ['completado', 'cancelado']:
            fecha_fin = historial_data.fecha_fin if historial_data.fecha_fin else historial.fecha_fin
            if not fecha_fin:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Los servicios completados o cancelados deben tener fecha de finalización"
                )
        
        # Si se cambia a "en_progreso", verificar que no haya otro historial activo
        if historial_data.estado == 'en_progreso':
            servicio_id = historial_data.IDservicio if historial_data.IDservicio else historial.IDservicio
            historial_activo = self.repository.get_historial_activo_servicio(servicio_id)
            if historial_activo and historial_activo.IDhistorial != historial_id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Ya existe un historial en progreso para este servicio"
                )
        
        return self.repository.update(historial_id, historial_data)
    
    def delete(self, historial_id: int) -> bool:
        historial = self.repository.get_by_id(historial_id)
        if not historial:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Historial de servicio no encontrado"
            )
        return self.repository.delete(historial_id)
    
    def get_by_servicio(self, servicio_id: int) -> List[HistorialServicioResponse]:
        from repositories.servicio_repository import ServicioRepository
        servicio_repo = ServicioRepository(self.repository.session)
        servicio = servicio_repo.get_by_id(servicio_id)
        
        if not servicio:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Servicio no encontrado"
            )
        
        return self.repository.get_by_servicio(servicio_id)
    
    def get_by_estado(self, estado: str) -> List[HistorialServicioResponse]:
        if estado not in ['completado', 'cancelado', 'en_progreso']:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Estado no válido. Use: completado, cancelado o en_progreso"
            )
        
        return self.repository.get_by_estado(estado)
    
    def get_by_fecha_rango(self, fecha_inicio: datetime, fecha_fin: datetime) -> List[HistorialServicioResponse]:
        if fecha_fin <= fecha_inicio:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="La fecha de fin debe ser posterior a la fecha de inicio"
            )
        
        return self.repository.get_by_fecha_rango(fecha_inicio, fecha_fin)
    
    def iniciar_servicio(self, servicio_id: int, notas: str = None) -> HistorialServicioResponse:
        """
        Método especial para iniciar un servicio (crea un historial en_progreso)
        """
        from repositories.servicio_repository import ServicioRepository
        servicio_repo = ServicioRepository(self.repository.session)
        servicio = servicio_repo.get_by_id(servicio_id)
        
        if not servicio:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Servicio no encontrado"
            )
        
        # Verificar que no haya un historial activo
        historial_activo = self.repository.get_historial_activo_servicio(servicio_id)
        if historial_activo:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El servicio ya está en progreso"
            )
        
        historial_data = HistorialServicioCreate(
            IDservicio=servicio_id,
            fecha_inicio=datetime.now(),
            estado='en_progreso',
            notas=notas
        )
        
        return self.repository.create(historial_data)
    
    def finalizar_servicio(self, servicio_id: int, estado: str, notas: str = None) -> HistorialServicioResponse:
        """
        Método especial para finalizar un servicio (completado o cancelado)
        """
        if estado not in ['completado', 'cancelado']:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Estado no válido para finalización. Use: completado o cancelado"
            )
        
        # Obtener el historial activo
        historial_activo = self.repository.get_historial_activo_servicio(servicio_id)
        if not historial_activo:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No hay un servicio en progreso para finalizar"
            )
        
        # Actualizar el historial
        update_data = HistorialServicioUpdate(
            fecha_fin=datetime.now(),
            estado=estado,
            notas=notas
        )
        
        return self.repository.update(historial_activo.IDhistorial, update_data)