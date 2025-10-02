from sqlalchemy.orm import Session
from sqlalchemy import func, text
from typing import List, Optional
from app.models.propietario import Propietario
from app.schemas.propietario import PropietarioCreate, PropietarioUpdate

class PropietarioRepository:
    def __init__(self, session: Session):
        self.session = session
    
    def get_all(self, skip: int=0, limit:int=100) -> List[Propietario]:
        """Obtener todos los propietarios paginados"""
        return self.session.query(Propietario).offset(skip).limit(limit).all()
    
    def get_by_id(self, propietario_id:int)-> Optional[Propietario]:
        """Obtener propietario por ID"""
        return self.session.query(Propietario).filter(Propietario.IDpropietario == propietario_id).first()
    
    def get_by_phone(self, telefono:str) -> Optional[Propietario]:
        return self.session.query(Propietario).filter(Propietario.telefono_propietario == telefono).first()
    
    def get_by_email(self, email:str)->Optional[Propietario]:
        """Obtener propietario por email"""
        return self.session.query(Propietario).filter(Propietario.correo_electronico_propietario == email).first()
    
    def create(self, propietario_data: PropietarioCreate)->Propietario:
        db_propietario = Propietario(**propietario_data.model_dump())
        self.session.add(db_propietario)
        self.session.commit()
        self.session.refresh(db_propietario)
        return db_propietario
    
    def update(self, propietario_id:int, propietario_data: PropietarioUpdate)-> Optional[Propietario]:
        db_propietario = self.get_by_id(propietario_id)
        if db_propietario:
            update_data = propietario_data.model_dump(exclude_unset=True)
            for field, value in update_data.items():
                setattr(db_propietario, field, value)
            self.session.commit()   
            self.session.refresh(db_propietario)
        return db_propietario
    
    def delete(self, propietario_id:int)-> bool:
        db_propietario = self.get_by_id(propietario_id)
        if db_propietario:
            self.session.delete(db_propietario)
            self.session.commit()
            return True
        return False
    
    def get_total_count(self)-> int:
        return self.session.query(func.count(Propietario.IDpropietario)).scalar()
    
    def search_by_name(self, search_term: str)->List[Propietario]:
        return self.session.query(Propietario).filter(
            func.concat(Propietario.nombres,' ', Propietario.apellidos).like(f'{search_term}')
        ).all()
    
    def get_by_city(self, ciudad:str)->List[Propietario]:
        return self.session.query(Propietario).filter(
            Propietario.ciudad_propietario == ciudad
        ).all()
