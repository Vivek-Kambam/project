# add the env enviroment here
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_USER = "CHARAN"
DATABASE_PASSWORD ="CHARAN2001"
DATABASE_HOST = "HOSTIUNG"
DATABASE_PORT = "5432"

