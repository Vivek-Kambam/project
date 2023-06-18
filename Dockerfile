FROM ubuntu:18.04

COPY . /app

WORKDIR /app

RUN pip3 install --upgrade pip

RUN pip3 install fastapi peewee requests python-dotenv uvicorn peewee-migrate pandas psycopg2-binary openpyxl telethon telebot python-telegram-bot telegram


EXPOSE 8000

CMD [ "sh", "deploy.sh" ]