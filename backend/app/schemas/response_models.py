from typing import Generic, TypeVar, List, Optional
from pydantic import BaseModel, ConfigDict, Field

T = TypeVar('T')

class APIResponse(BaseModel, Generic[T]):
    """Respuesta estandar de la Api"""
    success: bool = Field(..., description="Indica si la operacion fue exitosa")
    message: str = Field(..., description="Mensaje descriptivo de la operacion")
    data: Optional[T] = Field(None, description="Datos de respuesta")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example":{
                "success": True,
                "message": "Operacion realizada con exito",
                "data":{}
            }
        }
    )

class PaginatedResponse(BaseModel, Generic[T]):
    """Paginada Estandar"""
    items: List[T] = Field(..., description="Lista de elementos")
    total: int = Field(..., description="Total de elementos", example=86)
    page: int = Field(..., description="Pagina actual", example=1)
    per_page: int= Field(..., description="Elementos por pagina", example=10)
    total_pages: int= Field(..., description="Total de paginas", example=9)
    has_next: bool = Field(..., description="Tiene pagina siguiente")
    has_prev: bool = Field(..., description="Tiene pagiana anterior")
    
class ErrorResponse(BaseModel):
    """Esquema para respuestas de error"""
    success: bool = Field(False, description="Siempre False para errores")
    message: str = Field(..., description="Mensaje de Error")
    error_code: Optional[str] = Field(None, description="Codigo de error especifico")
    details: Optional[dict] = Field(None, description="Detalles adicionales del error")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example":{
                "success": False,
                "message": "Error al procesar la solicitud",
                "error_code": "VALIDATION_ERROR",
                "details":{
                    "field": "email",
                    "issue": "Invalid email format"
                }
            }
        }
    )

class SuccessResponse(BaseModel):
    """Respuesta simple de exito"""
    success: bool = Field(True, description="Operacion exitosa")
    message: str = Field(..., description="Mensaje de exito")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example":{
                "success": True,
                "message": "Operacion completada exitosamente"
            }
        }
    )
