from fastapi import APIRouter, Depends, Body
from fastapi import status

from fastapi.logger import logger as fastapi_logger
import logging

from app.v1.schema import profesor_schema
from app.v1.service import profesor_service

from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user

from app.v1.utils.db import get_db

router = APIRouter(prefix="/api/v1/profesor")
logging.getLogger(__name__)

@router.post(
    "/",
    tags=["profesor"],
    status_code=status.HTTP_201_CREATED,
    response_model=profesor_schema.Profesor,
    dependencies=[Depends(get_db)]
)
def create_profesor(profesor: profesor_schema.ProfesorBase = Body(...), current_user: User = Depends(get_current_user)):
    """
    ## Create a new profesor in the app

    ### Args
    The app can receive next fields into a JSON
    - nombre: Name of the profesor
    - apellido: Last name of the profesor
    - telefono: Phone number of the profesor
    - email: Email of the profesor

    ### Returns
    - profesor: Profesor info
    """
    fastapi_logger.info(f"Create profesor with data {profesor}")
    return profesor_service.create_profesor(profesor)

@router.get(
    "/{profesor_id}",
    tags=["profesor"],
    status_code=status.HTTP_200_OK,
    response_model=profesor_schema.Profesor,
    dependencies=[Depends(get_db)]
)
def get_profesor(profesor_id: int):
    """
    ## Get profesor by your id

    ### Args
    The app can receive next fields into a JSON
    - profesor_id: Id of the profesor

    ### Returns
    - profesor: Profesor info
    """
    fastapi_logger.info(f"Get profesor with id {profesor_id}")
    return profesor_service.get_profesor(profesor_id)

@router.get(
    "/",
    tags=["profesor"],
    status_code=status.HTTP_200_OK,
    response_model=list[profesor_schema.Profesor],
    dependencies=[Depends(get_db)]
)
def get_profesor():
    """
    ## Get all profesores in the app

    ### Returns
    - list of profesor: Profesor info for item
    """
    fastapi_logger.info(f"Get profesores")
    return profesor_service.get_profesores()
