from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repository.calificacion_cuidador import CalificacionCuidadorRepository
from app.schemas.calificacion_cuidador import CalificacionCuidadorCreate, CalificacionCuidadorUpdate, CalificacionCuidadorResponse, CalificacionCuidadorDetailed
from app.models.calificacion_cuidador import CalificacionCuidador

class CalificacionCuidadorService:
    def __init__(self, repository: CalificacionCuidadorRepository):
        self.repository = repository
    
    def get_all(self, skip: int = 0, limit: int = 10) -> List[CalificacionCuidadorResponse]:
        return self.repository.get_all(skip, limit)
    
    def get_by_id(self, calificacion_id: int) -> Optional[CalificacionCuidadorResponse]:
        calificacion = self.repository.get_by_id(calificacion_id)
        if not calificacion:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Calificación no encontrada"
            )
        return calificacion
    
    def get_detailed_by_id(self, calificacion_id: int) -> Optional[CalificacionCuidadorDetailed]:
        calificacion = self.repository.get_detailed_by_id(calificacion_id)
        if not calificacion:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Calificación no encontrada"
            )
        return calificacion
    
    def create(self, calificacion_data: CalificacionCuidadorCreate) -> CalificacionCuidadorResponse:
        # Verificar si el propietario existe
        from repositories.propietario_repository import PropietarioRepository
        propietario_repo = PropietarioRepository(self.repository.session)
        propietario = propietario_repo.get_by_id(calificacion_data.IDpropietario)
        
        if not propietario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Propietario no encontrado"
            )
        
        # Verificar si el cuidador existe
        from repositories.cuidador_repository import CuidadorRepository
        cuidador_repo = CuidadorRepository(self.repository.session)
        cuidador = cuidador_repo.get_by_id(calificacion_data.IDcuidador)
        
        if not cuidador:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Cuidador no encontrado"
            )
        
        # Verificar si el servicio existe
        from repositories.servicio_repository import ServicioRepository
        servicio_repo = ServicioRepository(self.repository.session)
        servicio = servicio_repo.get_by_id(calificacion_data.IDservicio)
        
        if not servicio:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Servicio no encontrado"
            )
        
        # Verificar que el servicio pertenece al propietario
        if servicio.IDpropietario != calificacion_data.IDpropietario:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El servicio no pertenece al propietario especificado"
            )
        
        # Verificar que no existe ya una calificación para este servicio
        if self.repository.existe_calificacion_servicio(calificacion_data.IDservicio, calificacion_data.IDpropietario):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe una calificación para este servicio"
            )
        
        return self.repository.create(calificacion_data)
    
    def update(self, calificacion_id: int, calificacion_data: CalificacionCuidadorUpdate) -> Optional[CalificacionCuidadorResponse]:
        calificacion = self.repository.get_by_id(calificacion_id)
        if not calificacion:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Calificación no encontrada"
            )
        
        return self.repository.update(calificacion_id, calificacion_data)
    
    def delete(self, calificacion_id: int) -> bool:
        calificacion = self.repository.get_by_id(calificacion_id)
        if not calificacion:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Calificación no encontrada"
            )
        return self.repository.delete(calificacion_id)
    
    def get_by_cuidador(self, cuidador_id: int) -> List[CalificacionCuidadorResponse]:
        from repositories.cuidador_repository import CuidadorRepository
        cuidador_repo = CuidadorRepository(self.repository.session)
        cuidador = cuidador_repo.get_by_id(cuidador_id)
        
        if not cuidador:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Cuidador no encontrado"
            )
        
        return self.repository.get_by_cuidador(cuidador_id)
    
    def get_by_propietario(self, propietario_id: int) -> List[CalificacionCuidadorResponse]:
        from repositories.propietario_repository import PropietarioRepository
        propietario_repo = PropietarioRepository(self.repository.session)
        propietario = propietario_repo.get_by_id(propietario_id)
        
        if not propietario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Propietario no encontrado"
            )
        
        return self.repository.get_by_propietario(propietario_id)
    
    def get_by_servicio(self, servicio_id: int) -> List[CalificacionCuidadorResponse]:
        from repositories.servicio_repository import ServicioRepository
        servicio_repo = ServicioRepository(self.repository.session)
        servicio = servicio_repo.get_by_id(servicio_id)
        
        if not servicio:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Servicio no encontrado"
            )
        
        return self.repository.get_by_servicio(servicio_id)
    
    def get_promedio_cuidador(self, cuidador_id: int) -> Dict[str, Any]:
        from repositories.cuidador_repository import CuidadorRepository
        cuidador_repo = CuidadorRepository(self.repository.session)
        cuidador = cuidador_repo.get_by_id(cuidador_id)
        
        if not cuidador:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Cuidador no encontrado"
            )
        
        promedio = self.repository.get_promedio_cuidador(cuidador_id)
        total_calificaciones = len(self.repository.get_by_cuidador(cuidador_id))
        
        return {
            "cuidador_id": cuidador_id,
            "promedio": round(promedio, 2) if promedio else 0.0,
            "total_calificaciones": total_calificaciones,
            "cuidador_nombre": cuidador.nombre_cuidador
        }
    
    def get_estadisticas_cuidador(self, cuidador_id: int) -> Dict[str, Any]:
        from repositories.cuidador_repository import CuidadorRepository
        cuidador_repo = CuidadorRepository(self.repository.session)
        cuidador = cuidador_repo.get_by_id(cuidador_id)
        
        if not cuidador:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Cuidador no encontrado"
            )
        
        # Obtener todas las calificaciones del cuidador
        calificaciones = self.repository.get_by_cuidador(cuidador_id)
        total = len(calificaciones)
        
        if total == 0:
            return {
                "cuidador_id": cuidador_id,
                "cuidador_nombre": cuidador.nombre_cuidador,
                "total_calificaciones": 0,
                "promedio": 0.0,
                "distribucion": {i: 0 for i in range(1, 6)}
            }
        
        # Calcular distribución por puntuación
        distribucion = {i: 0 for i in range(1, 6)}
        suma_puntuaciones = 0
        
        for calificacion in calificaciones:
            distribucion[calificacion.puntuacion] += 1
            suma_puntuaciones += calificacion.puntuacion
        
        promedio = suma_puntuaciones / total
        
        return {
            "cuidador_id": cuidador_id,
            "cuidador_nombre": cuidador.nombre_cuidador,
            "total_calificaciones": total,
            "promedio": round(promedio, 2),
            "distribucion": distribucion
        }