# Importamos todos los schemas
from .base import BaseSchema

# Propietario schemas
from .propietario import ( PropietarioBase, PropietarioCreate, PropietarioUpdate, PropietarioResponse, PropietarioWithMascotas)

# Mascota schemas
from .mascota import ( MascotaBase, MascotaCreate, MascotaUpdate, MascotaResponse, MascotaWithPropietario)

# Cuidador schemas
from .cuidador import ( TipoCuidador, CuidadorBase, CuidadorCreate, CuidadorUpdate, CuidadorResponse, CuidadorWithCalificaciones)

# Servicio schemas
from .servicio import ( ServicioBase, ServicioCreate, ServicioUpdate, ServicioResponse, ServicioDetailed)

# Agenda schemas
from .agenda import ( AgendaBase, AgendaCreate, AgendaUpdate, AgendaResponse, AgendaWithServicio)

# Historial schemas
from .historial_servicio import ( EstadoServicio, HistorialServicioBase, HistorialServicioCreate, HistorialServicioUpdate, HistorialServicioResponse, HistorialServicioWithServicio,
)

# Calificación schemas
from .calificacion_cuidador import ( CalificacionCuidadorBase, CalificacionCuidadorCreate, CalificacionCuidadorUpdate, CalificacionCuidadorResponse, CalificacionCuidadorDetailed)

# Resolver referencias circulares
PropietarioWithMascotas.model_rebuild()
MascotaWithPropietario.model_rebuild()
CuidadorWithCalificaciones.model_rebuild()
ServicioDetailed.model_rebuild()
AgendaWithServicio.model_rebuild()
HistorialServicioWithServicio.model_rebuild()
CalificacionCuidadorDetailed.model_rebuild()

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
]
