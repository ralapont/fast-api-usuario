from datetime import datetime
from pydantic import ValidationError

from fastapi import HTTPException, status

from fastapi.logger import logger as fastapi_logger

from app.v1.model.profesor_model import Profesor as ProfesorModel
from app.v1.model.clase_model import Clase as ClaseModel
from app.v1.schema import clase_schema

def create_clase(clase: clase_schema.ClaseBase):

    db_profesor = ProfesorModel.get(ProfesorModel.profesor_id==clase.profesor_id)

    db_clase = ClaseModel(
        cod_curso=clase.cod_curso,
        fecha_inicio_curso=clase.fecha_inicio_curso,
        fecha_fin_curso=clase.fecha_fin_curso,
        horario=clase.horario,
        profesor_id=db_profesor
    )

    db_clase.save(db_clase)

    return clase_schema.Clase(
        clase_id = db_clase.clase_id,
        cod_curso=db_clase.cod_curso,
        fecha_inicio_curso=db_clase.fecha_inicio_curso,
        fecha_fin_curso=db_clase.fecha_fin_curso,
        horario=db_clase.horario,
        profesor_id=db_profesor.profesor_id
    )

def get_clases():
    db_clases = ClaseModel.select()
    return map(lambda x : convert_entity_to_schema(x), db_clases)

def get_clase(clase_id: int):
    try:
        db_clase = ClaseModel.get(ClaseModel.clase_id==clase_id)
        return convert_entity_to_schema(db_clase)
    
    except ClaseModel.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Clase not found"
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

def convert_date_to_str(date: datetime): 
    date.strftime("%Y-%m-%d")
    #datestr = date.strftime("%Y-%m-%d")
    fecha = str(date.day) + "-" + str(date.month) + "-" + str(date.year)
    fastapi_logger.info(f"Fecha ==>  {fecha}")
    return date
    


            



