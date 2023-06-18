from fastapi import APIRouter


telegram_router = APIRouter()


@telegram_router.get('/get_mesages_from_channel')
def get_mesages_from_channel():
    try:
        return True
    except:
        return False
    

