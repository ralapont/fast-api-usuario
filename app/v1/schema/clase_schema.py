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
        description="Formato: DD-MM-YYYY",
        example="25-01-2025"
    )
    fecha_fin_curso: str = Field(
        ...,
        description="Formato: DD-MM-YYYY",
        example="28-01-2025"
    )
    horario: str = Field(
        ...,
        min_length=3,
        max_length=9,
        example="Mañanas"
    )
    profesor_id: int = Field(
        ...,
        example="5"
    )

    @model_validator(mode="after")
    def validar_fechas(cls, valores):
        try:
            # Convertimos ambas fechas al formato esperado (DD-MM-YYYY)
            fecha_inicio_curso = datetime.strptime(valores.fecha_inicio_curso, "%d-%m-%Y")
            fecha_fin_curso = datetime.strptime(valores.fecha_fin_curso, "%d-%m-%Y")
        except ValueError:
            raise ValueError("Ambas fechas deben estar en el formato DD-MM-YYYY.")
        
        # Validamos que la fecha de inicio sea anterior a la fecha de fin
        if fecha_inicio_curso >= fecha_fin_curso:
            raise ValueError("La fecha de inicio debe ser anterior a la fecha de fin.")

        valores.fecha_inicio_curso = fecha_inicio_curso.strftime("%d-%m-%Y")
        valores.fecha_fin_curso = fecha_fin_curso.strftime("%d-%m-%Y")        

        return valores
    
class Clase(ClaseBase):
    clase_id: int = Field(
        ...,
        example="5"
    )

