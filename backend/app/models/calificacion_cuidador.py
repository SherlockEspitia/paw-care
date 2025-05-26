from .base import Base, relationships
from sqlalchemy import Column, BigInteger, Integer, Text, DateTime, ForeignKey, CheckConstraint
from datetime import datetime

class CalificacionCuidador(Base):
    __tablename__ = 'calificacion_cuidador'
    
    IDcalificacion = Column(BigInteger, primary_key=True, autoincrement=True)
    IDpropietario = Column(BigInteger, ForeignKey('propietario.IDpropietario'), nullable=False)
    IDcuidador = Column(BigInteger, ForeignKey('cuidador.IDcuidador'), nullable=False)
    IDservicio = Column(BigInteger, ForeignKey('servicio.IDservicio'), nullable=False)
    puntuacion = Column(Integer, CheckConstraint('puntuacion BETWEEN 1 AND 5'), nullable=False)
    comentario = Column(Text)
    fecha_calificacion = Column(DateTime, default=datetime.utcnow)
    
    # Relaciones
    propietario = relationships("Propietario")
    cuidador = relationships("Cuidador", back_populates="calificaciones")
    servicio = relationships("Servicio", back_populates="calificaciones")