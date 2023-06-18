print("Hello Project")
# from fastapi import
from config import env
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from database.database_session import db
from libraries.authentication import *
# from database.create_table import create_database_table
# from database.migrations.migrate import create_migration
# from database.migrations.migrate import run_migration
from routers.telegram_routes import telegram_router
from routers.profiles_routes import profile_router

docs_url ="/docs"
app = FastAPI(docs_url= docs_url, debug=True)


app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"],
)
@app.on_event("startup")
def start():
    if db.is_closed():
        db.connect()
    
    # create_database_table()
    # create_migration()
    # run_migration()
    session_open()

@app.on_event("shutdown")
def stop():
    if not db.is_closed():
        db.close()
    
    session_close()

@app.get('/')
def welcome():
    return {"Project": "Hello welcome to the new Project"}



app.include_router(prefix="/profile_route", router=profile_router)
app.include_router(prefix="/telegram_route", router=telegram_router)