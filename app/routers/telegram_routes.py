from fastapi import APIRouter
from database.interactions.telegram_api.send_message_via_bot import telegram_message
from database.interactions.telegram_api.post_messages_to_users_and_channels import post_messages_to_users
from database.interactions.telegram_api.get_unread_messages import get_unread_messages_from_telegram_using_user


telegram_router = APIRouter()


@telegram_router.post('/post_messages_using_bot')
def post_messages_using_bot(message_to_channel : str = None, message_to_users: str = None):
    return post_messages_to_users(message_to_channel, message_to_users)

    

@telegram_router.post('/post_bot_message')
def post_bot_message():
    return telegram_message()


@telegram_router.get('/get_unread_messages_from_telegram')
async def get_unread_messages_from_telegram(username: str):
    return await get_unread_messages_from_telegram_using_user(username)