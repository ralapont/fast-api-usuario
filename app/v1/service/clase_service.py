from pydantic import ValidationError

from fastapi import HTTPException, status

from fastapi.logger import logger as fastapi_logger

from app.v1.model.profesor_model import Profesor as ProfesorModel
from app.v1.model.clase_model import Clase as ClaseModel
from app.v1.schema import clase_schema

def create_clase(clase: clase_schema.ClaseRequest):
    try:
        db_profesor = ProfesorModel.get(ProfesorModel.profesor_id==clase.profesor_id)
    except ProfesorModel.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profesor not found"
        )
    db_clase = ClaseModel.create(**clase.model_dump())
    db_clase.save()
    return clase_schema.Clase.model_validate(db_clase, from_attributes=True)

def modify_clase(clase_id: int, clase: clase_schema.ClaseRequest):

    query = ClaseModel.update(**clase.model_dump()).where(ClaseModel.clase_id == clase_id)
    rows = query.execute()
    if rows == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Clase not found"
        )

    db_clase = ClaseModel.get(ClaseModel.clase_id == clase_id)
    return clase_schema.Clase.model_validate(db_clase, from_attributes=True)

def delete_clase(clase_id: int):
    try:
        db_clase = ClaseModel.get(ClaseModel.clase_id==clase_id)
        db_clase.delete_instance()
    
    except ClaseModel.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Clase not found"
        )


def get_clases():
    db_clases = ClaseModel.select()
    return map(lambda x : clase_schema.Clase.model_validate(x, from_attributes=True), db_clases)

def get_clase(clase_id: int):
    try:
        db_clase = ClaseModel.get(ClaseModel.clase_id==clase_id)
        return clase_schema.Clase.model_validate(db_clase, from_attributes=True)
    
    except ClaseModel.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Clase not found"
        )

def get_clase_By_Profesor(profesor_id: int):
    try:
        profesor = ProfesorModel.get(ProfesorModel.profesor_id==profesor_id)
        db_clases = ClaseModel.select().where(ClaseModel.profesor==profesor)
        return map(lambda x : clase_schema.Clase.model_validate(x, from_attributes=True), db_clases)
    
    except ProfesorModel.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profesor not found"
        )
    
def convert_entity_to_schema(db_clase: ClaseModel):

    try:
        return clase_schema.Clase(
            clase_id=db_clase.clase_id,
            cod_curso=db_clase.cod_curso,
            fecha_inicio_curso=db_clase.fecha_inicio_curso.strftime("%Y-%m-%d"),
            fecha_fin_curso=db_clase.fecha_fin_curso.strftime("%Y-%m-%d"),
            horario=db_clase.horario,
            profesor_id=db_clase.profesor_id.profesor_id
        )
    except ValidationError as exc:
        print(repr(exc.errors()[0]['type']))




            



