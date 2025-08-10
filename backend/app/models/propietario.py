from .base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, String

class Propietario(Base):
    __tablename__ = 'propietario'
    
    IDpropietario = Column(BigInteger, primary_key=True, autoincrement=True)
    nombres = Column(String(45), nullable=False)
    apellidos = Column(String(45), nullable=False)
    correo_electronico_propietario = Column(String(75), nullable=False)
    telefono_propietario = Column(String(45), nullable=False, unique=True)
    direccion_propietario = Column(String(45), nullable=False)
    ciudad_propietario = Column(String(45), nullable=False)
    
    # Relación con mascotas
    mascotas = relationship("Mascota", back_populates="propietario")