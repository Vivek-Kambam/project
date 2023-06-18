# # # importing all required libraries  
# # import telebot  
# # from telethon.sync import TelegramClient  
# # from telethon.tl.types import InputPeerUser, InputPeerChannel  
# # from telethon import TelegramClient, sync, events  
# # from config.env import TELEGRAM_API_ID,TELEGRAM_API_HASH,bot_auth_token
# # # as said previously, obtain your API ID, API Hash, and Token from Telegram.  
# # # api_id = 'API_idin'  
# # # api_hash = 'API_hashing'  
# # # token = 'bot in token'  
# # # message = "Working..."  
# # # phone number  
# # phone = 'YOUR PHONE NUMBER WTH COUNTRY CODE'  
# # # establishing a telegraph session and   
# # # allocating it to a movable client  
# # def send_message_using_tele_bot(phone):
# #     client = TelegramClient('session', TELEGRAM_API_ID, TELEGRAM_API_HASH)  
# #     # creating the connection and the session  
# #     client.connect()  
# #     # If the script is run for the first time, it will prompt you to enter a token, an #OTPSentTo  
# #     # number, your Telegram ID, or both.  



# #     if not client.is_user_authorized():  
# #         client.send_code_request(phone)   
# #         # signing of the client  
# #         client.sign_in(phone, input('Enter the code: '))  
# #     try:  
# #         # Use   
# #     # my user id and access hash as a reference when   
# #     #using the receiver user-id and access-hash.  
# #         receiver = InputPeerUser('user_id', 'user_hash')  
# #         # using the Telegram client to send a message  
    
# #         client.send_message(receiverin, messagean, parse_mode='html')  
# #     except Exception as e:  
# #         # There may be numerous errors, such as peer   
# #     # error, incorrect access hash, flood error, etc.     
# #     print(e);  
# #     # cutting off the Telegram conversation  
# #     client.disconnect()  



# from telegram import Bot
# import tracemalloc
# tracemalloc.start()
# # from config.env import TELEGRAM_API_ID,TELEGRAM_API_HASH,bot_auth_token
# bot_auth_token = "6218429610:AAGlrVnRwq1RsvmuRjLOPaFKg54FxcptCVs"

def telegram_message():
    return True
#     print(":******************************************************************")
#     # Initialize the bot with your token
#     bot = Bot(token=bot_auth_token)

#     # Find the user ID based on the username
#     # updates = bot.getUpdates()
#     print(bot, "--------------------------------------------------------")
#     # for update in updates:
#     #     if update.message.chat.username == 'Vicky_511':
#     #         user_id = update.message.chat.id
#     #         break

#     # Send the message to the user
#     value = bot.sendMessage(chat_id='dnrkcharan', text='Hello, this is an automated message! from charan')
#     print( value, "--------------------------------------------------------")

#     return

# telegram_message(bot_auth_token)