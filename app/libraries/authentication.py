import requests

global authorisation_session


def session_open():
    global authorisation_session
    authorisation_session = requests.Session()


def session_close():
    global authorisation_session
    authorisation_session.close()