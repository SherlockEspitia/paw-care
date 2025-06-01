from pydantic import BaseModel, ConfigDict

class BaseSchema(BaseModel):
    """Schema base con configuración común"""
    model_config = ConfigDict(from_attributes=True)