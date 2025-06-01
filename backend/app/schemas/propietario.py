from pydantic import EmailStr, Field
from typing import Optional, List
from .base import BaseSchema

class PropietarioBase(BaseSchema):
    """Schema base para Propietario"""
    nombres: str = Field(..., max_length=45, description="Nombres del propietario")
    apellidos: str = Field(..., max_length=45, description="Apellidos del propietario")
    correo_electronico_propietario: EmailStr = Field(..., description="Correo electrónico del propietario")
    telefono_propietario: str = Field(..., max_length=45, description="Teléfono del propietario")
    direccion_propietario: str = Field(..., max_length=45, description="Dirección del propietario")
    ciudad_propietario: str = Field(..., max_length=45, description="Ciudad del propietario")

class PropietarioCreate(PropietarioBase):
    """Schema para crear un propietario"""
    
    pass

class PropietarioUpdate(BaseSchema):
    """Schema para actualizar un propietario"""
    nombres: Optional[str] = Field(None, max_length=45)
    apellidos: Optional[str] = Field(None, max_length=45)
    correo_electronico_propietario: Optional[EmailStr] = None
    telefono_propietario: Optional[str] = Field(None, max_length=45)
    direccion_propietario: Optional[str] = Field(None, max_length=45)
    ciudad_propietario: Optional[str] = Field(None, max_length=45)

class PropietarioResponse(PropietarioBase):
    """Schema para respuesta de propietario"""
    IDpropietario: int
    
class PropietarioWithMascotas(PropietarioResponse):
    """Schema de propietario con sus mascotas"""
    mascotas: List['MascotaResponse'] = []