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
            



