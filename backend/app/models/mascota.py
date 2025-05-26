from .base import Base, relationships
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
    propietario = relationships("Propietario", back_populates="mascotas")
    servicios = relationships("Servicio", back_populates="mascota")
