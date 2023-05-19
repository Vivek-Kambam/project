FROM ubuntu:18.04

COPY . /app

WORKDIR /app

RUN pip3 install --upgrade pip

RUN pip3 install fast-api peewee requests python-dotenv uvicorn


EXPOSE 8000

CMD [ "sh", "deploy.sh" ]