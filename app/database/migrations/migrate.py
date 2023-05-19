# auto create migrations 
from database.database_session import db 
from peewee_migrate import Router
import time
from pathlib import Path

current_directory : Path = Path.cwd()

default_migration_directory : Path = current_directory / "database" / "migrations"

router = Router(database = db, migration_dir = default_migration_directory)
timestamp = int(time.time())

def create_migration():
    router.create("migration_"+ str(timestamp))


def run_migration():
    router.run()

if __name__ == '__main__':
    create_migration()