import requests
from decouple import config


def sendPhotoOnTelegram(filename):
    file = {'photo': open(filename, 'rb')}
    res = requests.post(
        "https://api.telegram.org/bot{token}/sendPhoto?chat_id={chat_id}".format(token=config('TOKEN'), chat_id=config('CHAT_ID')),  files=file)
    print(res.status_code)
    if res.status_code == 200:
        print("Photo sent successfully!")
