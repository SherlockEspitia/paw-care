from pydantic import BaseModel, Field, validator
from typing import List, Optional
from datetime import datetime, date

class ValidationError(BaseModel):
    field: str = Field(..., description="Campo que causo el error")
    message: str = Field(..., description="Mensaje de error")
    code: str = Field(..., description="Codigo de error")

class BulkOperationRequest(BaseModel):
    ids: List[int] = Field(..., description="Lista de IDs a procesar", min_items=1)
    
    @validator('ids')
    def validate_unique_ids(cls, v):
        if len(v) != len(set(v)):
            raise ValueError('Los IDs deben ser unicos')
        return v

class BulkOperationResponse(BaseModel):
    success_count: int = Field(..., description="Numero de operaciones exitosas")
    error_count: int = Field(..., description="Numero de operaciones fallidas")
    errors: List[ValidationError] = Field(default=[], description="Lista de errores ocurridos")
    
class DateRange(BaseModel):
    star_date: date = Field(..., description="Fecha de inicio")
    end_date: date = Field(..., description="Fecha de fin")
    
    @validator('end_date')
    def validate_end_date(cls, v, values):
        if 'start_date' in values and v < values['start_date']:
            raise ValueError('La hora de fin debe ser posterior a la hora de inicio')
        return v

class HealthCheck(BaseModel):
    status: str = Field(..., description="Estado del servicio", example="healthy")
    timestamp: datetime = Field(..., description="Timestamp del check")
    version: str = Field(..., description="Version de la aplicacion", example="1.0.0")
    uptime: int = Field(..., description="Tiempo activo en segundos")
    
class StatsResponse(BaseModel):
    total_propietarios: int = Field(..., description="Total de propietarios")
    total_mascotas: int = Field(..., description="Total de mascotas")
    total_cuidadores: int = Field(..., description="Total de cuidadores")
    total_servicios: int = Field(..., description="Servicios activos")
    calificacion_promedio: Optional[float] = Field(None, description="Calificacion promedio global")
         