from fastapi import APIRouter
from database.interactions.telegram_api.send_message_via_bot import telegram_message
from database.interactions.telegram_api.get_messages_via_bot import get_messages


telegram_router = APIRouter()


@telegram_router.get('/get_mesages_from_channel')
def get_mesages_from_channel(text : str):
    try:
        return get_messages(text)
    except:
        return False
    

@telegram_router.post('/post_bot_message')
def post_bot_message():
    return telegram_message()

