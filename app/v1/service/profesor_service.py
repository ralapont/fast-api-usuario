from fastapi import HTTPException, status

from app.v1.model.profesor_model import Profesor as ProfesorModel
from app.v1.schema import profesor_schema

def create_profesor(profesor: profesor_schema.ProfesorBase):
    db_profesor = convert_schema_to_entity(profesor)    
    db_profesor.save(db_profesor)
    return convert_entity_to_schema(db_profesor)
            
def get_profesor(profesor_id: int):

    try:
        db_profesor = ProfesorModel.get(ProfesorModel.profesor_id==profesor_id)
    except ProfesorModel.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profesor not found"
        )

    return convert_entity_to_schema(db_profesor)

def get_profesores():

    db_profesors = ProfesorModel.select()
    return map(lambda x : convert_entity_to_schema(x), db_profesors)

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
    
    return convert_entity_to_schema(db_profesor)

def delete_profesor(profesor_id: int):
    try:
        db_profesor = ProfesorModel.get(ProfesorModel.profesor_id==profesor_id)
    except ProfesorModel.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profesor not found"
        )

    db_profesor.delete_instance()

def convert_entity_to_schema(profesor: ProfesorModel):
    return profesor_schema.Profesor(
        profesor_id = profesor.profesor_id,
        nombre = profesor.nombre,
        apellido= profesor.apellido,
        telefono = profesor.telefono,
        email = profesor.email
    )

def convert_schema_to_entity(profesor: profesor_schema.ProfesorBase):
    return ProfesorModel(
        nombre=profesor.nombre,
        apellido=profesor.apellido,
        telefono=profesor.telefono,
        email=profesor.email
    )    


