from pydantic import Field, validator
from typing import Optional
from datetime import datetime
from enum import Enum
from schemas.base import BaseSchema
#from schemas.servicio import ServicioResponse

class EstadoServicio(str, Enum):
    """Estados disponibles para el servicio"""
    COMPLETADO = "completado"
    CANCELADO = "cancelado"
    EN_PROGRESO = "en_progreso"

class HistorialServicioBase(BaseSchema):
    """Schema base para HistorialServicio"""
    fecha_inicio: datetime = Field(..., description="Fecha y hora de inicio del servicio")
    fecha_fin: Optional[datetime] = Field(None, description="Fecha y hora de finalización del servicio")
    estado: EstadoServicio = Field(..., description="Estado del servicio")
    notas: Optional[str] = Field(None, description="Notas adicionales del servicio")
    
    @validator('fecha_fin')
    def validar_fecha_fin(cls, v, values):
        """Validar que la fecha de fin sea posterior a la fecha de inicio"""
        if v and 'fecha_inicio' in values and values['fecha_inicio']:
            if v <= values['fecha_inicio']:
                raise ValueError('La fecha de fin debe ser posterior a la fecha de inicio')
        return v

class HistorialServicioCreate(HistorialServicioBase):
    """Schema para crear un historial de servicio"""
    IDservicio: int = Field(..., description="ID del servicio")

class HistorialServicioUpdate(BaseSchema):
    """Schema para actualizar un historial de servicio"""
    fecha_inicio: Optional[datetime] = None
    fecha_fin: Optional[datetime] = None
    estado: Optional[EstadoServicio] = None
    notas: Optional[str] = None
    
    @validator('fecha_fin')
    def validar_fecha_fin(cls, v, values):
        """Validar que la fecha de fin sea posterior a la fecha de inicio"""
        if v and 'fecha_inicio' in values and values['fecha_inicio']:
            if v <= values['fecha_inicio']:
                raise ValueError('La fecha de fin debe ser posterior a la fecha de inicio')
        return v

class HistorialServicioResponse(HistorialServicioBase):
    """Schema para respuesta de historial de servicio"""
    IDhistorial: int
    IDservicio: int

class HistorialServicioWithServicio(HistorialServicioResponse):
    """Schema de historial con información del servicio"""
    servicio: 'ServicioResponse'