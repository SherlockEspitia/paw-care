from pydantic import Field, validator
from typing import Optional
from datetime import date, time
from .base import BaseSchema
from .servicio import ServicioResponse

class AgendaBase(BaseSchema):
    """Schema base para Agenda"""
    fecha: Optional[date] = Field(None, description="Fecha de la cita")
    hora_inicio: Optional[time] = Field(None, description="Hora de inicio")
    hora_fin: Optional[time] = Field(None, description="Hora de finalización")
    
    @validator('hora_fin')
    def validar_hora_fin(cls, v, values):
        """Validar que la hora de fin sea posterior a la hora de inicio"""
        if v and 'hora_inicio' in values and values['hora_inicio']:
            if v <= values['hora_inicio']:
                raise ValueError('La hora de fin debe ser posterior a la hora de inicio')
        return v

class AgendaCreate(AgendaBase):
    """Schema para crear una agenda"""
    IDservicio: int = Field(..., description="ID del servicio")

class AgendaUpdate(BaseSchema):
    """Schema para actualizar una agenda"""
    fecha: Optional[date] = None
    hora_inicio: Optional[time] = None
    hora_fin: Optional[time] = None
    IDservicio: Optional[int] = None
    
    @validator('hora_fin')
    def validar_hora_fin(cls, v, values):
        """Validar que la hora de fin sea posterior a la hora de inicio"""
        if v and 'hora_inicio' in values and values['hora_inicio']:
            if v <= values['hora_inicio']:
                raise ValueError('La hora de fin debe ser posterior a la hora de inicio')
        return v

class AgendaResponse(AgendaBase):
    """Schema para respuesta de agenda"""
    IDagenda: int
    IDservicio: int

class AgendaWithServicio(AgendaResponse):
    """Schema de agenda con información del servicio"""
    servicio: 'ServicioResponse'