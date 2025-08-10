from .base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, String, Date, ForeignKey

class Mascota(Base):
    __tablename__ = 'mascota'
    
    IDmascota = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre_mascota = Column(String(45), nullable=False)
    especie = Column(String(45), nullable=False)
    raza = Column(String(45))
    fecha_nacimiento_mascota = Column(Date)
    IDpropietario = Column(BigInteger, ForeignKey('propietario.IDpropietario'), nullable=False)
    
    # Relaciones
    propietario = relationship("Propietario", back_populates="mascotas")
    servicios = relationship("Servicio", back_populates="mascota")
