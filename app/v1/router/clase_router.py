from fastapi import APIRouter, Depends, Body
from fastapi import status

from app.v1.schema import clase_schema
from app.v1.service import clase_service

from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

from app.v1.utils.db import get_db


router = APIRouter(prefix="/api/v1/clase")

@router.post(
    "/",
    tags=["clase"],
    status_code=status.HTTP_201_CREATED,
    response_model=clase_schema.Clase,
    dependencies=[Depends(get_db)]
)
def create_clase(clase: clase_schema.ClaseBase = Body(...), current_user: User = Depends(get_current_user)):
    """
    ## Create a new clase for a profesor in the app

    ### Args
    The app can receive next fields into a JSON
    - cod_curso: Code of the course
    - fecha_inicio_curso: Start date of the course
    - fecha_fin_curso: End date of the course
    - horario: Schedule of the course
    - profesor_id: Id of the profesor

    ### Returns
    - clase: Clase info
    """
    return clase_service.create_clase(clase)

