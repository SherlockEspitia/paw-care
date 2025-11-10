from .base import Base
from sqlalchemy import Column, Integer, BigInteger, Date, Time, ForeignKey
from sqlalchemy.orm import relationship

class Agenda(Base):
    __tablename__ = 'agenda'
    
    IDagenda = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(Date)
    hora_inicio = Column(Time)
    hora_fin = Column(Time)
    IDservicio = Column(BigInteger, ForeignKey('servicio.IDservicio'), nullable=False)
    
    # Relaciones
    servicio = relationship("Servicio", back_populates="agendas")