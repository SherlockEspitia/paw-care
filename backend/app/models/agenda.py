from .base import Base, relationships
from sqlalchemy import Column, Integer, BigInteger, Date, Time, ForeignKey

class Agenda(Base):
    __tablename__ = 'Agenda'
    
    IDagenda = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(Date)
    hora_inicio = Column(Time)
    hora_fin = Column(Time)
    IDservicio = Column(BigInteger, ForeignKey('servicio.IDservicio'), nullable=False)
    
    # Relaciones
    servicio = relationships("Servicio", back_populates="agendas")