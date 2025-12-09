from sqlalchemy import Column, Integer, String, Boolean
from .base import Base

class User(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password= Column(String)
    role = Column(String, default='propietario') # 'propiestario'|'cuidador'
    is_active = Column(Boolean, default=True)
