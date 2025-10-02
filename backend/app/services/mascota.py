from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repository.mascota import MascotaRepository
from app.repository.propietario import PropietarioRepository
from app.schemas.mascota import MascotaCreate, MascotaUpdate, MascotaResponse, MascotaWithPropietario
from app.models.mascota import Mascota

class MascotaService:
    def __init__(self, repository:MascotaRepository):
        self.repository =repository
        
    def get_all(self, skip:int = 0, limit:int=10)->List[MascotaResponse]:
        return self.repository.get_all(skip, limit)
    
    def get_by_id(self, mascota_id:int)-> Optional[MascotaWithPropietario]:
        mascota = self.repository.get_by_id(mascota_id)
        if not mascota:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Mascota no encontrada"
            )
        return mascota
    
    def create(self, mascota_data:MascotaCreate)-> MascotaResponse:
        repo_propietario = PropietarioRepository(self.repository.session)
        propietario = repo_propietario.get_by_id(mascota_data.IDpropietario)
        
        if not propietario:
            raise HTTPException(
                status_code= status.HTTP_404_NOT_FOUND,
                detail="Propietario no encontrado"
            )
        return self.repository.create(mascota_data)
    
    def update(self, mascota_id:int, mascota_data:MascotaUpdate)->Optional[MascotaResponse]:
        mascota = self.repository.get_by_id(mascota_id)
        if not mascota:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Mascota no encontrada")
        
        if mascota_data.IDpropietario:
           repo_propietario = PropietarioRepository(self.repository.session)
           propietario = repo_propietario.get_by_id(mascota_data.IDpropietario)
           
           if not propietario:
               raise HTTPException(
                   status_code=status.HTTP_404_NOT_FOUND,
                   detail="Propietario no encontrado"
               )
        
        return self.repository.update(mascota_id, mascota_data)
    
    def delete(self, mascota_id:int):
        mascota = self.repository.get_by_id(mascota_id)
        if not mascota:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Mascota no encontrada"
            )
        return self.repository.delete(mascota_id)
    
    def get_by_propietario(self, propietario_id:int)->List[MascotaResponse]:
        repo_repository = PropietarioRepository(self.repository.session)
        propietario = repo_repository.get_by_id(propietario_id)
        
        if not propietario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Propietario no encontrado"
            )
        
        return self.repository.session.query(Mascota).filter(
            Mascota.IDpropietario == propietario_id
        ).all()