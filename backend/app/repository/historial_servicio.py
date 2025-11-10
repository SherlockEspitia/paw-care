from typing import List, Optional
from sqlalchemy.orm import Session, joinedload
from datetime import datetime
from app.models.historial_servicio import HistorialServicio
from app.schemas.historial_servicio import HistorialServicioCreate, HistorialServicioUpdate

class HistorialServicioRepository:
    def __init__(self, session: Session):
        self.session = session
    
    def get_all(self, skip: int = 0, limit: int = 10) -> List[HistorialServicio]:
        return self.session.query(HistorialServicio).offset(skip).limit(limit).all()
    
    def get_by_id(self, historial_id: int) -> Optional[HistorialServicio]:
        return self.session.query(HistorialServicio).filter(HistorialServicio.IDhistorial == historial_id).first()
    
    def get_with_servicio(self, historial_id: int) -> Optional[HistorialServicio]:
        return self.session.query(HistorialServicio).options(
            joinedload(HistorialServicio.servicio)
        ).filter(HistorialServicio.IDhistorial == historial_id).first()
    
    def create(self, historial_data: HistorialServicioCreate) -> HistorialServicio:
        db_historial = HistorialServicio(**historial_data.model_dump())
        self.session.add(db_historial)
        self.session.commit()
        self.session.refresh(db_historial)
        return db_historial
    
    def update(self, historial_id: int, historial_data: HistorialServicioUpdate) -> Optional[HistorialServicio]:
        db_historial = self.get_by_id(historial_id)
        if db_historial:
            update_data = historial_data.model_dump(exclude_unset=True)
            for field, value in update_data.items():
                setattr(db_historial, field, value)
            self.session.commit()
            self.session.refresh(db_historial)
        return db_historial

    def delete(self, historial_id: int) -> bool:
        db_historial = self.get_by_id(historial_id)
        if db_historial:
            self.session.delete(db_historial)
            self.session.commit()
            return True
        return False
    
    def get_by_servicio(self, servicio_id: int) -> List[HistorialServicio]:
        return self.session.query(HistorialServicio).filter(HistorialServicio.IDservicio == servicio_id).all()
    
    def get_by_estado(self, estado: str) -> List[HistorialServicio]:
        return self.session.query(HistorialServicio).filter(HistorialServicio.estado == estado).all()
    
    def get_by_fecha_rango(self, fecha_inicio: datetime, fecha_fin: datetime) -> List[HistorialServicio]:
        """
        Obtiene historiales de servicio dentro de un rango de fechas
        """
        return self.session.query(HistorialServicio).filter(
            HistorialServicio.fecha_inicio >= fecha_inicio,
            HistorialServicio.fecha_inicio <= fecha_fin
        ).all()
    
    def get_historial_activo_servicio(self, servicio_id: int) -> Optional[HistorialServicio]:
        """
        Obtiene el historial activo (en_progreso) de un servicio
        """
        return self.session.query(HistorialServicio).filter(
            HistorialServicio.IDservicio == servicio_id,
            HistorialServicio.estado == 'en_progreso'
        ).first()