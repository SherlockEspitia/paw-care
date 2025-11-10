from pydantic import Field
from typing import Optional, List
from decimal import Decimal
from app.schemas.base import BaseSchema
from app.schemas.cuidador import CuidadorResponse
from app.schemas.mascota import MascotaResponse
from app.schemas.propietario import PropietarioResponse
from app.schemas.agenda import AgendaResponse
from app.schemas.historial_servicio import HistorialServicioResponse
from app.schemas.calificacion_cuidador import CalificacionCuidadorResponse

class ServicioBase(BaseSchema):
    """Schema base para Servicio"""
    descripcion_servicio: Optional[str] = Field(None, description="Descripción del servicio")
    precio: Optional[Decimal] = Field(None, ge=0, max_digits=10, decimal_places=2, description="Precio del servicio")
    tipo_servicio: Optional[str] = Field(None, max_length=45, description="Tipo de servicio")

class ServicioCreate(ServicioBase):
    """Schema para crear un servicio"""
    IDcuidador: int = Field(..., description="ID del cuidador")
    IDmascota: int = Field(..., description="ID de la mascota")
    IDpropietario: int = Field(..., description="ID del propietario")

class ServicioUpdate(BaseSchema):
    """Schema para actualizar un servicio"""
    IDcuidador: Optional[int] = None
    descripcion_servicio: Optional[str] = None
    precio: Optional[Decimal] = Field(None, ge=0, max_digits=10, decimal_places=2)
    IDmascota: Optional[int] = None
    IDpropietario: Optional[int] = None
    tipo_servicio: Optional[str] = Field(None, max_length=45)

class ServicioResponse(ServicioBase):
    """Schema para respuesta de servicio"""
    IDservicio: int
    IDcuidador: int
    IDmascota: int
    IDpropietario: int

class ServicioDetailed(ServicioResponse):
    """Schema detallado de servicio con relaciones"""
    cuidador: 'CuidadorResponse'
    mascota: 'MascotaResponse'
    propietario_rel: 'PropietarioResponse'
    agendas: List['AgendaResponse'] = []
    historial: Optional['HistorialServicioResponse'] = None
    calificaciones: List['CalificacionCuidadorResponse'] = []