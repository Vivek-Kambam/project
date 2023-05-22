import datetime
from peewee import *
from database.database_session import db
from playhouse.postgres_ext import *

class BaseModel(Model):
    class Meta:
        database = db

class Profile(BaseModel):
    id = PrimaryKeyField()
    username = CharField(unique=True)
    about = TextField()
    first_name = CharField()
    last_name = CharField()
    created_date = DateTimeField(default=datetime.datetime.now)
    updated_date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        db_table = "profile"