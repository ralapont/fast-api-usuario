from pydantic import BaseModel, model_validator
from pydantic import Field
from datetime import date, datetime
from typing import Any, ClassVar


class ClaseBase(BaseModel):
    cod_curso: str = Field(
        ...,
        min_length=3,
        max_length=10,
        example="Codigo"
    )
    fecha_inicio_curso: str = Field(
        ...,
        description="Formato: YYYY-MM-DD",
        example="2025-04-01"
    )
    fecha_fin_curso: str = Field(
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
    profesor_id: int = Field(
        ...,
        example=5
    )

    @model_validator(mode="after")
    def validar_fechas(cls, valores):
        try:
            # Convertimos ambas fechas al formato esperado (YYYY-MM-DD)
            fecha_inicio_curso = datetime.strptime(valores.fecha_inicio_curso, "%Y-%m-%d")
            fecha_fin_curso = datetime.strptime(valores.fecha_fin_curso, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Ambas fechas deben estar en el formato YYYY-MM-DD.")
        
        # Validamos que la fecha de inicio sea anterior a la fecha de fin
        if fecha_inicio_curso >= fecha_fin_curso:
            raise ValueError("La fecha de inicio debe ser anterior a la fecha de fin.")

        valores.fecha_inicio_curso = fecha_inicio_curso.strftime("%Y-%m-%d")
        valores.fecha_fin_curso = fecha_fin_curso.strftime("%Y-%m-%d")        

        return valores
    
class Clase(ClaseBase):
    clase_id: int = Field(
        ...,
        example=5
    )

