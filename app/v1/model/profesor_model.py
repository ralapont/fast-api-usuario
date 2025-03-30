import peewee as pw

from app.v1.utils.db import db

class Profesor(pw.Model):
   profesor_id = pw.AutoField()
   nombre = pw.CharField()
   apellido = pw.CharField()
   telefono = pw.CharField()
   email = pw.CharField(unique=True)

   class Meta:
       database = db