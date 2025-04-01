from app.v1.model.user_model import User as UserModel
from app.v1.model.profesor_model import Profesor as ProfesorModel
from app.v1.model.clase_model import Clase as ClaseModel

from app.v1.utils.db import db

db.create_tables([UserModel, ProfesorModel, ClaseModel], safe=True)
print("Create tables User, Profesor and Clase")