from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from repository.cuidador import CuidadorRepository
from schemas.cuidador import CuidadorCreate, CuidadorUpdate, CuidadorResponse, CuidadorWithCalificaciones, CuidadorAvailable

class CuidadorService:
    def __init__(self):
        self.repository = CuidadorRepository