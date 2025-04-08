import peewee as pw

from app.v1.utils.db import db

class User(pw.Model):
    user_id = pw.AutoField()
    email = pw.CharField(unique=True, index=True)
    username = pw.CharField(unique=True, index=True)
    password = pw.CharField()

    class Meta:
        database = db