from pydantic import BaseModel, model_validator
from pydantic import Field
from datetime import datetime, date

from app.v1.schema import profesor_schema

class ClaseBase(BaseModel):
    cod_curso: str = Field(
        ...,
        min_length=3,
        max_length=10,
        example="Codigo"
    )
    fecha_inicio_curso: date = Field(
        ...,
        description="Formato: YYYY-MM-DD",
        example="2025-04-01"
    )
    fecha_fin_curso: date = Field(
        ...,
        description="Formato: YYYY-MM-DD",
        example="2025-05-01"
    )
    horario: str = Field(
        ...,
        min_length=3,
        max_length=9,
        example="Mañanas"
    )

    @model_validator(mode="after")
    def validar_fechas(cls, valores):
        # Validamos que la fecha de inicio sea anterior a la fecha de fin
        if valores.fecha_inicio_curso >= valores.fecha_fin_curso:
            raise ValueError("La fecha de inicio debe ser anterior a la fecha de fin.")

        return valores

class Clase(ClaseBase):
    clase_id: int = Field(
        ...,
        example=5
    )
    profesor: profesor_schema.Profesor

class ClaseRequest(ClaseBase):
    profesor_id: int = Field(
        ...,
        example=5
    )
    
