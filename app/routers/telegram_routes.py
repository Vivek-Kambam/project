from fastapi import APIRouter
from database.interactions.telegram_api.send_message_via_bot import telegram_message
from database.interactions.telegram_api.get_messages_via_bot import post_messages_to_users


telegram_router = APIRouter()


@telegram_router.post('/get_mesages_from_channel')
def get_mesages_from_channel(message_to_channel : str = None, message_to_users: str = None):
    return post_messages_to_users(message_to_channel, message_to_users)

    

@telegram_router.post('/post_bot_message')
def post_bot_message():
    return telegram_message()

