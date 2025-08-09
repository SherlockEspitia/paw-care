from fastapi import APIRouter, Depends, Query, Path, status
from sqlalchemy.orm import Session
from typing import List, Optional
from connection import get_db
from schemas.propietario import (PropietarioCreate, PaginatedResponse, PropietarioList, PropietarioSummary)
from services.propietario import PropietarioService

router = APIRouter(
    prefix="/propietarios",
    tags = ["Propietarios"],
    responses={404:{"description": "No encontrado"}}
)

@router.get("/", response_model=PropietarioList, summary="Listar propietarios", description="Obtener lista paginada de propietarios registrados")
async def get_propietarios( page: int = Query(default=1, ge=1, description="Número de Pagina"), 
    per_page:int = Query(default=10, ge=1, le=100, description="Elementos por pagina"), session:Session=Depends(get_db)):
    service = PropietarioService(session)
    return service.get_propietario_paginated(page=page, per_page=per_page)
