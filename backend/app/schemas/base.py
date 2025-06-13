from pydantic import BaseModel, ConfigDict

class BaseSchema(BaseModel):
    """Schema base con configuración común"""
    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True,
        str_strip_whitespace=True,
        json_schema_extra={
            "example":{}
        }
    )