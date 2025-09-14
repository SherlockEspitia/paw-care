from sqlalchemy.orm import Session
from sqlalchemy import func, text
from typing import List, Optional
from models.cuidador import Cuidador
from schemas.cuidador import CuidadorCreate, CuidadorUpdate

class CuidadorRepository:
    def __init__(self, session:Session):
        self.session = session
    
    def get_all(self, skip:int = 0, limit:int= 100) -> List[Cuidador]:
        return self.session.query(Cuidador).offset(skip).limit(limit).all()
    
    def get_by_id(self, cuidador_id:str)-> Optional[Cuidador]:
        return self.session.query(Cuidador).filter( Cuidador.IDcuidador == cuidador_id).first()
    
    def get_by_phone(self, telefono:str)->Optional[Cuidador]:
        return self.session.query(Cuidador).filter(Cuidador.telefono_cuidador == telefono).first()
    
    def get_by_email(self, email:str) -> Optional[Cuidador]:
        return self.session.query(Cuidador).filter(Cuidador.correo_electronico_cuidador == email).first()
    
    def create(self, cuidador_data:CuidadorCreate)->Cuidador:
        db_cuidador = Cuidador(**cuidador_data.model_dump())
        self.session.add(db_cuidador)
        self.session.commit()
        self.session.refresh(db_cuidador)
        return db_cuidador
    
    def update(self, cuidador_id:int, cuidador_data:CuidadorUpdate)->Optional[Cuidador]:
        db_cuidador=self.get_by_id(cuidador_id)
        if db_cuidador:
            update_data = cuidador_data.model_dump(exclude_unset=True)
            for field, value in update_data.items():
                setattr(db_cuidador, field, value)
            self.session.commit()
            self.session.refresh(db_cuidador)
        return db_cuidador
    
    def delete(self, cuidador_id:int) -> bool:
        db_cuidador = self.get_by_id(cuidador_id)
        if db_cuidador:
            self.session.delete(db_cuidador)
            self.session.commit()
            return True
        return False
    
    def get_total_count(self)->int:
        return self.session.query(func.count(Cuidador.IDcuidador)).scalar()
    
    def search_by_name(self, search_tearm:str)->List[Cuidador]:
        return self.session.query(Cuidador).filter(
            func.concat(Cuidador.nombre_cuidador).like(f'{search_tearm}')
        ).all()
    
    def get_by_city(self, especialidad:str)->List[Cuidador]:
        return self.session.query(Cuidador).filter(
            Cuidador.especialidad == especialidad
        ).all()   
    