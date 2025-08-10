from .base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, String, Text, DECIMAL, ForeignKey

class Servicio(Base):
    __tablename__ = 'servicio'
    
    IDservicio = Column(BigInteger, primary_key=True, autoincrement=True)
    IDcuidador = Column(BigInteger, ForeignKey('cuidador.IDcuidador'), nullable=False)
    descripcion_servicio = Column(Text)
    precio = Column(DECIMAL(10, 2))
    IDmascota = Column(BigInteger, ForeignKey('mascota.IDmascota'), nullable=False)
    IDpropietario = Column(BigInteger, ForeignKey('propietario.IDpropietario'), nullable=False)
    tipo_servicio = Column(String(45))
    
    # Relaciones
    cuidador = relationship("Cuidador", back_populates="servicios")
    mascota = relationship("Mascota", back_populates="servicios")
    propietario_rel = relationship("Propietario")
    agendas = relationship("Agenda", back_populates="servicio")
    historial = relationship("HistorialServicio", uselist=False, back_populates="servicio")
    calificaciones = relationship("CalificacionCuidador", back_populates="servicio")