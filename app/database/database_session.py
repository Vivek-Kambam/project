from peewee import *
from config.env import *

db = PostgresqlDatabase(
    DATABASE_NAME,
    autorollback=True,
    user = DATABASE_USER,
    password = DATABASE_PASSWORD,
    host = DATABASE_HOST,
    port = DATABASE_PORT

)