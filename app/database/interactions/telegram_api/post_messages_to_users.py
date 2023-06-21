import requests
from config.env import BOT_AUTH_TOKEN


def post_messages_to_users(message_to_channel, message_to_users):
    try:
        all_result=[]
        get_users_url = "https://api.telegram.org/bot"+ BOT_AUTH_TOKEN + "/getUpdates"
        get_users_list = requests.get(get_users_url)
        get_all_users = get_users_list.json()
        channel_list = []
        user_list = []

        for every_user in get_all_users["result"]:
            if every_user.get("channel_post") and message_to_channel is not None and every_user["channel_post"]["sender_chat"]['id'] not in channel_list:
                url = "https://api.telegram.org/bot" + BOT_AUTH_TOKEN + "/sendMessage?chat_id=" + str(every_user["channel_post"]["sender_chat"]['id']) + "&text=" + message_to_channel
                result = requests.get(url)
                result_ = result.json()
                channel_list.append(every_user["channel_post"]["sender_chat"]['id'])
            if every_user.get("message") and every_user["message"]["from"]['id'] == 1193552586 and message_to_users is not None and every_user["message"]["from"]['id'] not in user_list:
                url = "https://api.telegram.org/bot" + BOT_AUTH_TOKEN + "/sendMessage?chat_id=" + str(every_user["message"]["from"]['id']) + "&text=" + message_to_users
                result = requests.get(url)
                result_ = result.json()
                print(result_)
                user_list.append(every_user["message"]["from"]['id'])
            else:
                continue
            
            # all_result.append(result_)            
        
        return True
    except:
        raise