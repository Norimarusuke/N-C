from peewee import *


db = SqliteDatabase('s-c-b.db')

class Person(Model):
    name = CharField()
    age = IntegerField()
    gender = CharField()
    class Meta:
        database = db # This model uses the "people.db" database.

db.create_tables([Person])