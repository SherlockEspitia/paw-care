from .cuidador import router as cuidador_router
from .propietario import router as propietario_router
from .mascota import router as mascota_router
from .servicio import router as servicio_router
from .agenda import router as agenda_router

__all__=[
    cuidador_router,
    propietario_router,
    mascota_router,
    servicio_router,
    agenda_router
]