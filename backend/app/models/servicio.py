from .base import Base, relationships
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
    cuidador = relationships("Cuidador", back_populates="servicios")
    mascota = relationships("Mascota", back_populates="servicios")
    propietario_rel = relationships("Propietario")
    agendas = relationships("Agenda", back_populates="servicio")
    historial = relationships("HistorialServicio", uselist=False, back_populates="servicio")
    calificaciones = relationships("CalificacionCuidador", back_populates="servicio")