import requests

def get_messages(text):
    token = "6218429610:AAGlrVnRwq1RsvmuRjLOPaFKg54FxcptCVs"
    username = "1786444932"

    url = "https://api.telegram.org/bot" + token + "/sendMessage?chat_id=" + username + "&text=" + text

    result = requests.get(url)

    return result.json()