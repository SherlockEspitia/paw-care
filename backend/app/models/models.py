# models.py
from sqlalchemy import Column, BigInteger, String, Date, Enum, Text, DECIMAL, Integer, DateTime, ForeignKey, Time, CheckConstraint
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

# Usamos la misma base declarativa para todos los modelos
Base = declarative_base()

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
    servicios = relationship("Servicio", back_populates="cuidador")
    calificaciones = relationship("CalificacionCuidador", back_populates="cuidador")

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

class Agenda(Base):
    __tablename__ = 'Agenda'
    
    IDagenda = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(Date)
    hora_inicio = Column(Time)
    hora_fin = Column(Time)
    IDservicio = Column(BigInteger, ForeignKey('servicio.IDservicio'), nullable=False)
    
    # Relaciones
    servicio = relationship("Servicio", back_populates="agendas")

class HistorialServicio(Base):
    __tablename__ = 'historial_servicio'
    
    IDhistorial = Column(BigInteger, primary_key=True, autoincrement=True)
    IDservicio = Column(BigInteger, ForeignKey('servicio.IDservicio'), nullable=False)
    fecha_inicio = Column(DateTime, nullable=False)
    fecha_fin = Column(DateTime)
    estado = Column(Enum('completado', 'cancelado', 'en_progreso'), nullable=False)
    notas = Column(Text)
    
    # Relación
    servicio = relationship("Servicio", back_populates="historial")

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
    propietario = relationship("Propietario")
    cuidador = relationship("Cuidador", back_populates="calificaciones")
    servicio = relationship("Servicio", back_populates="calificaciones")