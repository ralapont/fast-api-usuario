from fastapi import HTTPException, status

from app.v1.model.profesor_model import Profesor as ProfesorModel
from app.v1.schema import profesor_schema

def create_profesor(profesor: profesor_schema.ProfesorBase):
    db_profesor = ProfesorModel.create(**profesor.model_dump())
    db_profesor.save()
    return profesor_schema.Profesor.model_validate(db_profesor, from_attributes=True)
            
def get_profesor(profesor_id: int):

    try:
        db_profesor = ProfesorModel.get(ProfesorModel.profesor_id==profesor_id)
    except ProfesorModel.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profesor not found"
        )

    return profesor_schema.Profesor.model_validate(db_profesor, from_attributes=True)

def get_profesores():

    db_profesors = ProfesorModel.select()
    return map(lambda x : profesor_schema.Profesor.model_validate(x, from_attributes=True), db_profesors)

def modify_profesor(profesor_id: int, profesor: profesor_schema.ProfesorBase):
    try:
        db_profesor = ProfesorModel.get(ProfesorModel.profesor_id==profesor_id)
    except ProfesorModel.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profesor not found"
        )

    db_profesor.nombre = profesor.nombre
    db_profesor.apellido = profesor.apellido
    db_profesor.telefono = profesor.telefono
    db_profesor.email = profesor.email
    db_profesor.save()
    
    return profesor_schema.Profesor.model_validate(db_profesor, from_attributes=True)

def delete_profesor(profesor_id: int):
    try:
        db_profesor = ProfesorModel.get(ProfesorModel.profesor_id==profesor_id)
    except ProfesorModel.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profesor not found"
        )

    db_profesor.delete_instance()



