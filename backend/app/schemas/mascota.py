from pydantic import Field
from typing import Optional, List
from datetime import date
from .base import BaseSchema

class MascotaBase(BaseSchema):
    """Schema base para Mascota"""
    nombre_mascota: str = Field(..., max_length=45, description="Nombre de la mascota")
    especie: str = Field(..., max_length=45, description="Especie de la mascota")
    raza: Optional[str] = Field(None, max_length=45, description="Raza de la mascota")
    fecha_nacimiento_mascota: Optional[date] = Field(None, description="Fecha de nacimiento de la mascota")

class MascotaCreate(MascotaBase):
    """Schema para crear una mascota"""
    IDpropietario: int = Field(..., description="ID del propietario de la mascota")

class MascotaUpdate(BaseSchema):
    """Schema para actualizar una mascota"""
    nombre_mascota: Optional[str] = Field(None, max_length=45)
    especie: Optional[str] = Field(None, max_length=45)
    raza: Optional[str] = Field(None, max_length=45)
    fecha_nacimiento_mascota: Optional[date] = None
    IDpropietario: Optional[int] = None

class MascotaResponse(MascotaBase):
    """Schema para respuesta de mascota"""
    IDmascota: int
    IDpropietario: int

class MascotaWithPropietario(MascotaResponse):
    """Schema de mascota con información del propietario"""
    propietario: 'PropietarioResponse'