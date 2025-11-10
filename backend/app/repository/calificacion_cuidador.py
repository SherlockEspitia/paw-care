from typing import List, Optional
from sqlalchemy.orm import Session, joinedload
from app.models.calificacion_cuidador import CalificacionCuidador
from app.schemas.calificacion_cuidador import CalificacionCuidadorCreate, CalificacionCuidadorUpdate

class CalificacionCuidadorRepository:
    def __init__(self, session: Session):
        self.session = session
    
    def get_all(self, skip: int = 0, limit: int = 10) -> List[CalificacionCuidador]:
        return self.session.query(CalificacionCuidador).offset(skip).limit(limit).all()
    
    def get_by_id(self, calificacion_id: int) -> Optional[CalificacionCuidador]:
        return self.session.query(CalificacionCuidador).filter(CalificacionCuidador.IDcalificacion == calificacion_id).first()
    
    def get_detailed_by_id(self, calificacion_id: int) -> Optional[CalificacionCuidador]:
        return self.session.query(CalificacionCuidador).options(
            joinedload(CalificacionCuidador.propietario),
            joinedload(CalificacionCuidador.cuidador),
            joinedload(CalificacionCuidador.servicio)
        ).filter(CalificacionCuidador.IDcalificacion == calificacion_id).first()
    
    def create(self, calificacion_data: CalificacionCuidadorCreate) -> CalificacionCuidador:
        db_calificacion = CalificacionCuidador(**calificacion_data.model_dump())
        self.session.add(db_calificacion)
        self.session.commit()
        self.session.refresh(db_calificacion)
        return db_calificacion
    
    def update(self, calificacion_id: int, calificacion_data: CalificacionCuidadorUpdate) -> Optional[CalificacionCuidador]:
        db_calificacion = self.get_by_id(calificacion_id)
        if db_calificacion:
            update_data = calificacion_data.model_dump(exclude_unset=True)
            for field, value in update_data.items():
                setattr(db_calificacion, field, value)
            self.session.commit()
            self.session.refresh(db_calificacion)
        return db_calificacion

    def delete(self, calificacion_id: int) -> bool:
        db_calificacion = self.get_by_id(calificacion_id)
        if db_calificacion:
            self.session.delete(db_calificacion)
            self.session.commit()
            return True
        return False
    
    def get_by_cuidador(self, cuidador_id: int) -> List[CalificacionCuidador]:
        return self.session.query(CalificacionCuidador).filter(CalificacionCuidador.IDcuidador == cuidador_id).all()
    
    def get_by_propietario(self, propietario_id: int) -> List[CalificacionCuidador]:
        return self.session.query(CalificacionCuidador).filter(CalificacionCuidador.IDpropietario == propietario_id).all()
    
    def get_by_servicio(self, servicio_id: int) -> List[CalificacionCuidador]:
        return self.session.query(CalificacionCuidador).filter(CalificacionCuidador.IDservicio == servicio_id).all()
    
    def get_promedio_cuidador(self, cuidador_id: int) -> Optional[float]:
        """
        Calcula el promedio de calificaciones de un cuidador
        """
        result = self.session.query(
            Session.func.avg(CalificacionCuidador.puntuacion).label('promedio')
        ).filter(CalificacionCuidador.IDcuidador == cuidador_id).first()
        
        return result[0] if result[0] is not None else None
    
    def get_calificaciones_por_puntuacion(self, cuidador_id: int, puntuacion: int) -> List[CalificacionCuidador]:
        """
        Obtiene calificaciones específicas por puntuación
        """
        return self.session.query(CalificacionCuidador).filter(
            CalificacionCuidador.IDcuidador == cuidador_id,
            CalificacionCuidador.puntuacion == puntuacion
        ).all()
    
    def existe_calificacion_servicio(self, servicio_id: int, propietario_id: int) -> bool:
        """
        Verifica si ya existe una calificación para un servicio por parte de un propietario
        """
        calificacion = self.session.query(CalificacionCuidador).filter(
            CalificacionCuidador.IDservicio == servicio_id,
            CalificacionCuidador.IDpropietario == propietario_id
        ).first()
        
        return calificacion is not None