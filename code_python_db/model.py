from peewee import *

db = SqliteDatabase('database.db')

# ne pas changer cette classe
class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    name = CharField()

class Exercice(BaseModel):
    name = CharField()
   
class UserExercice(BaseModel):
    user = ForeignKeyField(User, backref='exercices')
    exercice = ForeignKeyField(Exercice, backref='users')
    nr_fois = IntegerField(null=True)
