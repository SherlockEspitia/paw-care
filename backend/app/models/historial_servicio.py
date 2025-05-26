from .base import Base, relationships
from sqlalchemy import Column, BigInteger, DateTime, Enum, Text, ForeignKey


class HistorialServicio(Base):
    __tablename__ = 'historial_servicio'
    
    IDhistorial = Column(BigInteger, primary_key=True, autoincrement=True)
    IDservicio = Column(BigInteger, ForeignKey('servicio.IDservicio'), nullable=False)
    fecha_inicio = Column(DateTime, nullable=False)
    fecha_fin = Column(DateTime)
    estado = Column(Enum('completado', 'cancelado', 'en_progreso'), nullable=False)
    notas = Column(Text)
    
    # Relación
    servicio = relationships("Servicios", back_populates="historial")