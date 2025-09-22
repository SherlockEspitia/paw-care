from .cuidador import router as cuidador_router
from .propietario import router as propietario_router
from .mascota import router as mascota_router
from .servicio import router as servicio_router
from .agenda import router as agenda_router
from .historial_servicio import router as historial_servicio_router
from .calificacion_cuidador import router as calificacion_cuidador_router

__all__=[
    cuidador_router,
    propietario_router,
    mascota_router,
    servicio_router,
    agenda_router,
    historial_servicio_router,
    calificacion_cuidador_router
]