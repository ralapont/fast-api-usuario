import peewee as pw
from app.v1.model.profesor_model import Profesor as ProfesorModel


from app.v1.utils.db import db
fmt = "%Y-%m-%d"

class Clase(pw.Model):
   clase_id = pw.AutoField()
   cod_curso = pw.CharField()
   fecha_inicio_curso = pw.DateField(formats=[fmt])
   fecha_fin_curso = pw.DateField(formats=[fmt])
   horario = pw.CharField()
   profesor = pw.ForeignKeyField(ProfesorModel)

   class Meta:
       database = db