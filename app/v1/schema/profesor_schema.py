from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr

class ProfesorBase(BaseModel):
    nombre: str = Field(
        ...,
        min_length=3,
        max_length=50,
        example="MyNombre"
    )
    apellido: str = Field(
        ...,
        min_length=3,
        max_length=50,
        example="MyApellido"
    )
    telefono: str = Field(
        ...,
        min_length=3,
        max_length=9,
        example="123456789"
    )
    email: EmailStr = Field(
        ...,
        example="myemail@cosasdedevs.com"
    )


class Profesor(ProfesorBase):
    profesor_id: int = Field(
        ...,
        example="5"
    )

