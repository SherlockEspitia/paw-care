from pydantic import ConfigDict, EmailStr, Field
from typing import Optional, List, TYPE_CHECKING
from schemas.base import BaseSchema

if TYPE_CHECKING:
    from schemas.mascota import MascotaResponse

class PropietarioBase(BaseSchema):
    """Schema base para Propietario"""
    nombres: str = Field(..., max_length=45, description="Nombres del propietario")
    apellidos: str = Field(..., max_length=45, description="Apellidos del propietario")
    correo_electronico_propietario: EmailStr = Field(..., description="Correo electrónico del propietario")
    telefono_propietario: str = Field(..., max_length=45, description="Teléfono del propietario")
    direccion_propietario: str = Field(..., max_length=45, description="Dirección del propietario")
    ciudad_propietario: str = Field(..., max_length=45, description="Ciudad del propietario")

class PropietarioCreate(PropietarioBase):
    """Schema para crear un propietario"""
    model_config = ConfigDict(
        json_schema_extra={
            "example":{
                "nombres": "Sergio Andres",
                "apellidos": "Cano Sosa",
                "correo_electronico_propietario": "sergiocano@email.com",
                "telefono_propietario":"+57 300 123 4567",
                "direccion_propietario":"Carrera 52 #12-34",
                "ciudad_propietario": "Medellín"
            }
        }
    )

class PropietarioUpdate(BaseSchema):
    """Schema para actualizar un propietario"""
    nombres: Optional[str] = Field(None, max_length=45)
    apellidos: Optional[str] = Field(None, max_length=45)
    correo_electronico_propietario: Optional[EmailStr] = None
    telefono_propietario: Optional[str] = Field(None, max_length=45)
    direccion_propietario: Optional[str] = Field(None, max_length=45)
    ciudad_propietario: Optional[str] = Field(None, max_length=45)
    
    model_config = ConfigDict(
        json_schema_extra={
            "example":{
                "nombres":"Juan Carlos",
                "telefono_propietario":"+57 300 987 6666"
            }
        }
    )

class PropietarioResponse(PropietarioBase):
    """Schema para respuesta de propietario"""
    IDpropietario: int = Field(..., description="Id unico del propietario", example=1)
    
class PropietarioWithMascotas(PropietarioResponse):
    """Schema de propietario con sus mascotas"""
    mascotas: List['MascotaResponse'] = Field(default=[], description="Lista de mascotas del propietario")
    
class PropietarioList(BaseSchema):
    """Listado de paginado de propietarios"""
    propietarios: List[PropietarioResponse]
    total: int = Field(..., description="Total de propietarios", example=100)
    page: int = Field(..., description="Pagina Actual", example=1)
    per_page: int = Field(..., description="Elementos por pagina", example=10)
    
class PropietarioSummary(BaseSchema):
    """Resumen de Listas de Usuario"""
    IDpropietario: int
    nombres: str
    apellidos: str
    telefono_propietario: str
    