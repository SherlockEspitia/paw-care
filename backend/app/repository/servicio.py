from typing import List, Optional
from sqlalchemy.orm import Session, joinedload
from app.models.servicio import Servicio
from app.schemas.servicio import ServicioCreate, ServicioUpdate

class ServicioRepository:
    def __init__(self, session:Session):
        self.session = session
        
    def get_all(self, skip:int = 0, limit:int=10)->List[Servicio]:
        return self.session.query(Servicio).offset(skip).limit(limit).all()
    
    def get_by_id(self, servicio_id:int)->Optional[Servicio]:
        return self.session.query(Servicio).filter(Servicio.IDservicio == servicio_id).first()
    
    def get_detailed_by_id(self, servicio_id: int)-> Optional[Servicio]:
        return self.session.query(Servicio).options(
            joinedload(Servicio.cuidador),
            joinedload(Servicio.mascota),
            joinedload(Servicio.propietario_rel),
            joinedload(Servicio.agendas),
            joinedload(Servicio.historial),
            joinedload(Servicio.calificaciones)
        ).filter(Servicio.IDservicio == servicio_id).first()
    
    def create(self, servicio_data: ServicioCreate)->Servicio:
        db_servicio = Servicio(**servicio_data.model_dump())
        self.session.add(db_servicio)
        self.session.commit()
        self.session.refresh(db_servicio)
        return db_servicio
    
    def update(self, servicio_id:int, servicio_data:ServicioUpdate)->Optional[Servicio]:
        db_servicio = self.get_by_id(servicio_id)
        if db_servicio:
            update_data = servicio_data.model_dump(exclude_unset=True)
            for field, value in update_data.items():
                setattr(db_servicio, field, value)
            self.session.commit()
            self.session.refresh(db_servicio)
        return db_servicio
    
    def delete(self, servicio_id:int)->bool:
        db_servicio = self.get_by_id(servicio_id)
        if db_servicio:
            self.session.delete(db_servicio)
            self.session.commit()
            return True
        return False
    
    def get_by_cuidador(self, cuidador_id:int)->List[Servicio]:
        return self.session.query(Servicio).filter(Servicio.IDcuidador== cuidador_id).all()
    
    def get_by_mascota(self, mascota_id:int)->List[Servicio]:
        return self.session.query(Servicio).filter(Servicio.IDmascota == mascota_id).all()
    
    def get_by_propietario(self, propietario_id:int)->List[Servicio]:
        return self.session.query(Servicio).filter(Servicio.IDpropietario == propietario_id).all()
