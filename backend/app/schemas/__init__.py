# Importamos todos los schemas
from schemas.base import BaseSchema

# Propietario schemas
from schemas.propietario import ( PropietarioBase, PropietarioCreate, PropietarioUpdate, PropietarioResponse, PropietarioWithMascotas, PropietarioList, PropietarioSummary)

# Mascota schemas
from schemas.mascota import ( MascotaBase, MascotaCreate, MascotaUpdate, MascotaResponse, MascotaWithPropietario)

# Cuidador schemas
from schemas.cuidador import ( TipoCuidador, CuidadorBase, CuidadorCreate, CuidadorUpdate, CuidadorResponse, CuidadorWithCalificaciones, CuidadorAvailable)

# Servicio schemas
from schemas.servicio import ( ServicioBase, ServicioCreate, ServicioUpdate, ServicioResponse, ServicioDetailed)

# Agenda schemas
from schemas.agenda import ( AgendaBase, AgendaCreate, AgendaUpdate, AgendaResponse, AgendaWithServicio)

# Historial schemas
from schemas.historial_servicio import ( EstadoServicio, HistorialServicioBase, HistorialServicioCreate, HistorialServicioUpdate, HistorialServicioResponse, HistorialServicioWithServicio,
)

# Calificación schemas
from schemas.calificacion_cuidador import ( CalificacionCuidadorBase, CalificacionCuidadorCreate, CalificacionCuidadorUpdate, CalificacionCuidadorResponse, CalificacionCuidadorDetailed)

# Modelos de respuestas y utilidades de FastAPI
from schemas.response_models import( APIResponse, PaginatedResponse, ErrorResponse, SuccessResponse)

from schemas.query_params import ( SortOrder, PaginationParams, SortParams, SearchParams, PropietarioQueryParams, MascotaQueryParams, CuidadorQueryParams, ServicioQueryParams, DateRangeParams)

from schemas.validation_models import (ValidationError, BulkOperationResponse, BulkOperationRequest, DateRange, HealthCheck, StatsResponse)

# Resolver referencias circulares
PropietarioWithMascotas.model_rebuild()
MascotaWithPropietario.model_rebuild()
CuidadorWithCalificaciones.model_rebuild()
ServicioDetailed.model_rebuild()
AgendaWithServicio.model_rebuild()
HistorialServicioWithServicio.model_rebuild()
CalificacionCuidadorDetailed.model_rebuild()
ServicioResponse.model_rebuild()

# Exportamos todo
__all__ = [
    # Base
    "BaseSchema",
    
    # Propietario
    "PropietarioBase",
    "PropietarioCreate",
    "PropietarioUpdate",
    "PropietarioResponse",
    "PropietarioWithMascotas",
    "PropietarioList",
    "PropietarioSummary",
    
    # Mascota
    "MascotaBase",
    "MascotaCreate",
    "MascotaUpdate",
    "MascotaResponse",
    "MascotaWithPropietario",
    
    # Cuidador
    "TipoCuidador",
    "CuidadorBase",
    "CuidadorCreate",
    "CuidadorUpdate",
    "CuidadorResponse",
    "CuidadorWithCalificaciones",
    "CuidadorAvailable",
    
    # Servicio
    "ServicioBase",
    "ServicioCreate",
    "ServicioUpdate",
    "ServicioResponse",
    "ServicioDetailed",
    
    # Agenda
    "AgendaBase",
    "AgendaCreate",
    "AgendaUpdate",
    "AgendaResponse",
    "AgendaWithServicio",
    
    # Historial
    "EstadoServicio",
    "HistorialServicioBase",
    "HistorialServicioCreate",
    "HistorialServicioUpdate",
    "HistorialServicioResponse",
    "HistorialServicioWithServicio",
    
    # Calificación
    "CalificacionCuidadorBase",
    "CalificacionCuidadorCreate",
    "CalificacionCuidadorUpdate",
    "CalificacionCuidadorResponse",
    "CalificacionCuidadorDetailed",
    
    #FastApi Response Models
    "APIResponse",
    "PaginatedResponse",
    "ErrorResponse",
    "SuccessResponse",
    
    #Query Parameters
    "SortOrder",
    "PaginationParams",
    "SortParams",
    "SearchParams",
    "PropietarioQueryParams",
    "MascotaQueryParams",
    "CuidadorQueryParams",
    "ServicioQueryParams",
    "DateRangeParams",
    
    #Validation Models
    "ValidationError",
    "BulkOperationRequest",
    "BulkOperationResponse",
    "DateRange",
    "TimeRange",
    "HealthCheck",
    "StatsResponse"
]
