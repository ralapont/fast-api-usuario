from app.v1.model.profesor_model import Profesor as ProfesorModel
from app.v1.schema import profesor_schema

def create_profesor(profesor: profesor_schema.ProfesorBase):
        
    db_profesor = ProfesorModel(
        nombre=profesor.nombre,
        apellido=profesor.apellido,
        telefono=profesor.telefono,
        email=profesor.email
    )

    db_profesor.save(db_profesor)

    return profesor_schema.Profesor(
        profesor_id = db_profesor.profesor_id,
        nombre=db_profesor.nombre,
        apellido=db_profesor.apellido,
        telefono=db_profesor.telefono,
        email=db_profesor.email
    )    
            
def get_profesor(profesor_id: int):

    db_profesor = ProfesorModel.get(profesor_id==profesor_id)

    return profesor_schema.Profesor(
        profesor_id = db_profesor.profesor_id,
        nombre=db_profesor.nombre,
        apellido=db_profesor.apellido,
        telefono=db_profesor.telefono,
        email=db_profesor.email
    )    



