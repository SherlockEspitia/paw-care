from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from repository.cuidador import CuidadorRepository
from schemas.cuidador import CuidadorCreate, CuidadorUpdate, CuidadorResponse, CuidadorWithCalificaciones, CuidadorAvailable

class CuidadorService:
    def __init__(self, session:Session):
        self.repository = CuidadorRepository(session)
    
    def get_cuidador_by_id(self, cuidador_id) -> CuidadorResponse:
        cuidador = self.repository.get_by_id(skip= skip, limit= per_page)
        if not cuidador:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = f"El cuidador con id:{cuidador_id} no encontrado"
            )
        return CuidadorResponse.model_validate(cuidador)

    def create_cuidador(self, cuidador_data:CuidadorCreate)-> CuidadorResponse:
        if self.repository.get_by_phone(cuidador_data.telefono_cuidador):
            raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail = "Ya existe un cuidador con ese numero de telefono"
            )
        if self.repository.get_by_email(cuidador_data.email_cuidador):
            raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail = "Ya existe un cuidador con ese email"
            )
        
        new_cuidador = self.repository.create(cuidador_data)
        return CuidadorResponse.model_validate(new_cuidador)
    
    def update_cuidador(self, cuidador_id:int, cuidador_data:CuidadorUpdate) -> CuidadorResponse:
        if not self.repository.get_by_id(cuidador_id):
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = f'Cuidador con ID {cuidador_id} no encontrado'
            )
        
        if cuidador_data.telefono_cuidador:
            existing_phone = self.repository.get_by_phone(cuidador_data.telefono_cuidador)
            if existing_phone and existing_phone.IDcuidador != cuidador_id:
                raise HTTPException(
                    status_code = status.HTTP_400_BAD_REQUEST,
                    detail = "Ya existe un cuidador con este numero de telefono"
                )
            
            update_cuidador = self.repository.update(cuidador_id, cuidador_data)
            return CuidadorResponse.model_validate(update_propietario)

    def delete_cuidador(self, cuidador_id:int)->dict:
        if not self.repository.delete(cuidador_id):
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND
                detail = f"Cuidador con ID{cuidador_id} no encontrado"
            )
        return { "message":"Cuidador eliminado exitosamente"}
    
    