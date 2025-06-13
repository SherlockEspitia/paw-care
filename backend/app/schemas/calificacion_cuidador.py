from pydantic import Field
from typing import Optional
from datetime import datetime
from .base import BaseSchema
from .propietario import PropietarioResponse
from .cuidador import CuidadorResponse
from .servicio import ServicioResponse

class CalificacionCuidadorBase(BaseSchema):
    """Schema base para CalificacionCuidador"""
    puntuacion: int = Field(..., ge=1, le=5, description="Puntuación del 1 al 5")
    comentario: Optional[str] = Field(None, description="Comentario sobre el servicio")

class CalificacionCuidadorCreate(CalificacionCuidadorBase):
    """Schema para crear una calificación"""
    IDpropietario: int = Field(..., description="ID del propietario que califica")
    IDcuidador: int = Field(..., description="ID del cuidador calificado")
    IDservicio: int = Field(..., description="ID del servicio calificado")

class CalificacionCuidadorUpdate(BaseSchema):
    """Schema para actualizar una calificación"""
    puntuacion: Optional[int] = Field(None, ge=1, le=5)
    comentario: Optional[str] = None

class CalificacionCuidadorResponse(CalificacionCuidadorBase):
    """Schema para respuesta de calificación"""
    IDcalificacion: int
    IDpropietario: int
    IDcuidador: int
    IDservicio: int
    fecha_calificacion: datetime

class CalificacionCuidadorDetailed(CalificacionCuidadorResponse):
    """Schema detallado de calificación con relaciones"""
    propietario: 'PropietarioResponse'
    cuidador: 'CuidadorResponse'
    servicio: 'ServicioResponse'