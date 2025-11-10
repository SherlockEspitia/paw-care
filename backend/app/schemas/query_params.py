from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum

class SortOrder(str, Enum):
    ASC = "asc"
    DESC = "desc"

class PaginationParams(BaseModel):
    page: int = Field(1, ge=1, description="Numero de pagina", example=1)
    per_page: int = Field(10, ge=1, le=100, description="Elementos por pagina", example=10)
    
class SortParams(BaseModel):
    sort_by: Optional[str] = Field(None, description="Campo por el cual ordenar", example="nombre_propietario")
    sort_order: SortOrder = Field(SortOrder.ASC, description="Orden de Clasificacion")
    
class SearchParams(BaseModel):
    search: Optional[str] = Field(None, min_length=1, description="Termino de Busqueda", example="Sergio")
    
class PropietarioQueryParams(PaginationParams, SortParams, SearchParams):
    ciudad: Optional[str] = Field(None, description="Filtrar por ciudad", example="Medellín")
    
class MascotaQueryParams(PaginationParams, SortParams, SearchParams):
    especie: Optional[str] = Field(None, description="Filtrar por especie", example="Perro")
    propietario_id: Optional[int] = Field(None, description="Filtrar por propietario", example=1)

class CuidadorQueryParams(PaginationParams, SortParams, SearchParams):
    tipo_cuidador: Optional[str] = Field(None, description="Filtrar por tipo", example="paseador")
    disponible: Optional[bool] = Field(None, description="Solo cuidadores disponibles")

class ServicioQueryParams(PaginationParams, SortParams):
    propietario_id: Optional[int] = Field(None, description="Filtar por propietario")
    cuidador_id: Optional[int] = Field(None, description="Filtrar por cuidador")
    tipo_servicio:Optional[int] = Field(None, description="Filtrar por tipo de servicio")

class DateRangeParams(BaseModel):
    fecha_inicio: Optional[str] = Field(None, description="Fecha inicio (YYYY-MM-DD)", example="2024-01-01")
    fecha_fin: Optional[str] = Field(None, description="Fecha fin (YYYY-MM-DD)", example="2024-12-31")