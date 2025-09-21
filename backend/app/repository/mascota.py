from sqlalchemy.orm import Session
from sqlalchemy import func, text
from typing import List, Optional
from app.models.mascota import Mascota
from app.schemas.mascota import MascotaCreate, MascotaUpdate, MascotaResponse, MascotaWithPropietario

class MascotaRepository:
    def __init__(self, session:Session):
        self.session = session
    
    def get_all(self, skip:int=0, limit:int=5)-> List[Mascota]:
        return self.session.query(Mascota).offset(skip).limit(limit).all()
    
    def get_by_id(self, mascota_id:int)-> Optional[Mascota]:
        return self.session.query(Mascota).filter(Mascota.IDmascota == mascota_id).first()
    
    def get_by_propietario(self, propietario_id:int)-> Optional[Mascota]:
        return self.db.query(Mascota).filter(Mascota.IDpropietario== propietario_id).all()
    
    def get_by_especie(self, especie:str):
        return self.session.query(Mascota).filter(Mascota.especie==especie).all()
        
    
    def create(self, mascota_data:MascotaCreate)->Mascota:
        db_mascota = Mascota(**mascota_data.model_dump())
        self.session.add(db_mascota)
        self.session.commit()
        self.session.refresh(db_mascota)
        return db_mascota
    
    def update(self, mascota_id:int, mascota_data: MascotaUpdate)->Optional[Mascota]:
        db_mascota = self.get_by_id(mascota_id)
        if db_mascota:
            update_data= mascota_data.model_dump(exclude_unset=True)
            for field, value in update_data.items():
                setattr(db_mascota, field, value)
            self.session.commit()
            self.session.refresh(db_mascota)
        return db_mascota

    def delete(self, mascota_id:int)->bool:
        db_mascota = self.get_by_id(mascota_id)
        if db_mascota:
            self.session.delete(db_mascota)
            self.session.commit()
            return True
        return False
    
    def exists(self, mascota_id:int)->bool:
        return self.db.query(Mascota).filter(Mascota.IDmascota==mascota_id).first() is not None
    