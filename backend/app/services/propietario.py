from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from repository.propietario import PropietarioRepository
from schemas.propietario import (PropietarioCreate, PropietarioUpdate, PropietarioResponse, PropietarioList, PropietarioSummary)

class PropietarioService:
    def __init__(self, session: Session):
        self.repository = PropietarioRepository(session)
    
    def get_propietario_paginated(self, page:int=1, per_page:int=10)-> PropietarioList:
        skip = (page-1)*per_page
        propietarios = self.repository.get_all(skip=skip, limit=per_page)
        total = self.repository.get_total_count()
        return PropietarioList(
            propietarios=[PropietarioResponse.model_validate(p) for p in propietarios],
            total=total,
            page=page,
            per_page=per_page
        )
    
    def get_propietario_by_id(self, propietario_id: int)->PropietarioResponse:
        propietario = self.repository.get_by_id(propietario_id)
        if not propietario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Propietario con ID {propietario_id} no encontrado"
            )
        return PropietarioResponse.model_validate(propietario)

    def create_propietario(self, propietario_data: PropietarioCreate)->PropietarioResponse:
        if self.repository.get_by_phone(propietario_data.telefono_propietario):
            raise HTTPException(
                status_code= status.HTTP_400_BAD_REQUEST,
                detail="Ya existe un propietario con este numero de telefono"
            )
        
        if self.repository.get_by_email(propietario_data.correo_electronico_propietario):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe un propietario con este correo electronico"
            )
