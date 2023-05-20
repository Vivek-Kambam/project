from database.database_session import db
from database.models.profiles import Profile

def create_database_table():
    try:
        db.create_tables([Profile])
        print("table created")
    
    except:
        print("error while creating the table")
        raise

if __name__ == "__main__":
    create_database_table()
