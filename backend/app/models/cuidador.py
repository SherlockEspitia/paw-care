from .base import Base, relationships
from sqlalchemy import Column, BigInteger, String, Enum, Text, DECIMAL, Integer

class Cuidador(Base):
    __tablename__ = 'cuidador'
    
    IDcuidador = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre_cuidador = Column(String(45), nullable=False)
    correo_electronico_cuidador = Column(String(45), nullable=False)
    telefono_cuidador = Column(String(45), nullable=False)
    tipo_cuidador = Column(Enum('paseador', 'entrenador', 'guarderia'), nullable=False)
    experiencia = Column(Integer)
    tarifas = Column(DECIMAL(10, 2))
    especialidad = Column(String(45))
    certificaciones = Column(Text)
    direccion = Column(String(125))
    capacidad = Column(Integer)
    
    # Relaciones
    servicios = relationships("Servicio", back_populates="cuidador")
    calificaciones = relationships("CalificacionCuidador", back_populates="cuidador")