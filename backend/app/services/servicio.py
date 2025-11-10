from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repository.servicio import ServicioRepository
from app.repository.cuidador import CuidadorRepository
from app.repository.mascota import MascotaRepository
from app.repository.propietario import PropietarioRepository
from app.schemas.servicio import ServicioCreate, ServicioUpdate, ServicioResponse, ServicioDetailed
from app.models.servicio import Servicio

class ServicioService:
    def __init__(self, repository: ServicioRepository):
        self.repository = repository
    
    def get_all(self, skip: int = 0, limit: int = 10) -> List[ServicioResponse]:
        return self.repository.get_all(skip, limit)
    
    def get_by_id(self, servicio_id: int) -> Optional[ServicioResponse]:
        servicio = self.repository.get_by_id(servicio_id)
        if not servicio:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Servicio no encontrado"
            )
        return servicio
    
    def get_detailed_by_id(self, servicio_id: int) -> Optional[ServicioDetailed]:
        servicio = self.repository.get_detailed_by_id(servicio_id)
        if not servicio:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Servicio no encontrado"
            )
        return servicio
    
    def create(self, servicio_data: ServicioCreate) -> ServicioResponse:
        # Verificar si el cuidador existe
        cuidador_repo = CuidadorRepository(self.repository.session)
        cuidador = cuidador_repo.get_by_id(servicio_data.IDcuidador)
        
        if not cuidador:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Cuidador no encontrado"
            )
        
        # Verificar si la mascota existe
        mascota_repo = MascotaRepository(self.repository.session)
        mascota = mascota_repo.get_by_id(servicio_data.IDmascota)
        
        if not mascota:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Mascota no encontrada"
            )
        
        # Verificar si el propietario existe
        propietario_repo = PropietarioRepository(self.repository.session)
        propietario = propietario_repo.get_by_id(servicio_data.IDpropietario)
        
        if not propietario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Propietario no encontrado"
            )
        
        return self.repository.create(servicio_data)
    
    def update(self, servicio_id: int, servicio_data: ServicioUpdate) -> Optional[ServicioResponse]:
        servicio = self.repository.get_by_id(servicio_id)
        if not servicio:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Servicio no encontrado"
            )
        
        # Si se está actualizando el cuidador, verificar que existe
        if servicio_data.IDcuidador:
            cuidador_repo = CuidadorRepository(self.repository.session)
            cuidador = cuidador_repo.get_by_id(servicio_data.IDcuidador)
            
            if not cuidador:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Cuidador no encontrado"
                )
        
        # Si se está actualizando la mascota, verificar que existe
        if servicio_data.IDmascota:
            mascota_repo = MascotaRepository(self.repository.session)
            mascota = mascota_repo.get_by_id(servicio_data.IDmascota)
            
            if not mascota:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Mascota no encontrada"
                )
        
        # Si se está actualizando el propietario, verificar que existe
        if servicio_data.IDpropietario:
            propietario_repo = PropietarioRepository(self.repository.session)
            propietario = propietario_repo.get_by_id(servicio_data.IDpropietario)
            
            if not propietario:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Propietario no encontrado"
                )
        
        return self.repository.update(servicio_id, servicio_data)
    
    def delete(self, servicio_id: int) -> bool:
        servicio = self.repository.get_by_id(servicio_id)
        if not servicio:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Servicio no encontrado"
            )
        return self.repository.delete(servicio_id)
    
    def get_by_cuidador(self, cuidador_id: int) -> List[ServicioResponse]:
        cuidador_repo = CuidadorRepository(self.repository.session)
        cuidador = cuidador_repo.get_by_id(cuidador_id)
        
        if not cuidador:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Cuidador no encontrado"
            )
        
        return self.repository.get_by_cuidador(cuidador_id)
    
    def get_by_mascota(self, mascota_id: int) -> List[ServicioResponse]:
        mascota_repo = MascotaRepository(self.repository.session)
        mascota = mascota_repo.get_by_id(mascota_id)
        
        if not mascota:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Mascota no encontrada"
            )
        
        return self.repository.get_by_mascota(mascota_id)
    
    def get_by_propietario(self, propietario_id: int) -> List[ServicioResponse]:
        propietario_repo = PropietarioRepository(self.repository.session)
        propietario = propietario_repo.get_by_id(propietario_id)
        
        if not propietario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Propietario no encontrado"
            )
        
        return self.repository.get_by_propietario(propietario_id)