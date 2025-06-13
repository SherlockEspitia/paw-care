from pydantic import ConfigDict, EmailStr, Field
from typing import Optional, List
from decimal import Decimal
from enum import Enum
from .base import BaseSchema
from .calificacion_cuidador import CalificacionCuidadorResponse

class TipoCuidador(str, Enum):
    """Tipos de cuidador disponibles"""
    PASEADOR = "paseador"
    ENTRENADOR = "entrenador"
    GUARDERIA = "guarderia"

class CuidadorBase(BaseSchema):
    """Schema base para Cuidador"""
    nombre_cuidador: str = Field(..., max_length=45, description="Nombre del cuidador")
    correo_electronico_cuidador: EmailStr = Field(..., description="Correo electrónico del cuidador")
    telefono_cuidador: str = Field(..., max_length=45, description="Teléfono del cuidador")
    tipo_cuidador: TipoCuidador = Field(..., description="Tipo de cuidador")
    experiencia: Optional[int] = Field(None, ge=0, description="Años de experiencia")
    tarifas: Optional[Decimal] = Field(None, ge=0, max_digits=10, decimal_places=2, description="Tarifas por servicio")
    especialidad: Optional[str] = Field(None, max_length=45, description="Especialidad del cuidador")
    certificaciones: Optional[str] = Field(None, description="Certificaciones del cuidador")
    direccion: Optional[str] = Field(None, max_length=125, description="Dirección del cuidador")
    capacidad: Optional[int] = Field(None, ge=1, description="Capacidad máxima de mascotas")

class CuidadorCreate(CuidadorBase):
    """Schema para crear un cuidador"""
    model_config = ConfigDict(        
        json_schema_extra= {
            "example": {
                "nombre_cuidador": "Ana López",
                "correo_electronico_cuidador": "ana.lopez@email.com",
                "telefono_cuidador": "+57 311 987 6543",
                "tipo_cuidador": "paseador",
                "experiencia": 3,
                "tarifas": "25000.00",
                "especialidad": "Perros grandes",
                "direccion": "Carrera 70 #25-15",
                "capacidad": 5
            }
        }    
    ) 

class CuidadorUpdate(BaseSchema):
    """Schema para actualizar un cuidador"""
    nombre_cuidador: Optional[str] = Field(None, max_length=45)
    correo_electronico_cuidador: Optional[EmailStr] = None
    telefono_cuidador: Optional[str] = Field(None, max_length=45)
    tipo_cuidador: Optional[TipoCuidador] = None
    experiencia: Optional[int] = Field(None, ge=0)
    tarifas: Optional[Decimal] = Field(None, ge=0, max_digits=10, decimal_places=2)
    especialidad: Optional[str] = Field(None, max_length=45)
    certificaciones: Optional[str] = None
    direccion: Optional[str] = Field(None, max_length=125)
    capacidad: Optional[int] = Field(None, ge=1)

class CuidadorResponse(CuidadorBase):
    """Schema para respuesta de cuidador"""
    IDcuidador: int

class CuidadorWithCalificaciones(CuidadorResponse):
    """Schema de cuidador con sus calificaciones"""
    calificaciones: List['CalificacionCuidadorResponse'] = Field(default=[], description="Lista de calificaciones del cuidador")
    promedio_calificacion: Optional[float] = Field(None, description="Promedio de calificaciones", example=4.5)
    total_calificaciones: int = Field(0, description="Total de calificaciones recibidas", example=16)
    
class CuidadorDisponible(BaseSchema):
    IDcuidador: int
    nombre_cuidador: str
    tipo_cuidador: TipoCuidador
    tarifas: Optional[Decimal]
    promedio_calificacion: Optional[float]
    capacidad_disponible: int = Field(..., description="Capacidad disponible actual")