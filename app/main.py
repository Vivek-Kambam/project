print("Hello Project")
# from fastapi import
from config import env
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from database.database_session import db
from libraries.authentication import *
from database.create_table import create_database_table

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
    session_open()

@app.on_event("shutdown")
def stop():
    if not db.is_closed():
        db.close()
    
    session_close()

@app.get('/')
def welcome():
    return {"Project": "Hello welcome to the new Project"}


