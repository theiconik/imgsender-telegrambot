import requests


def sendPhotoOnTelegram(filename):
    file = {'photo': open(filename, 'rb')}
    res = requests.post(
        "https://api.telegram.org/bot{token}/sendPhoto?chat_id={chat_id}".format(token="", chat_id=""),  files=file)
    print(res.status_code)
    if res.status_code == 200:
        print("Photo sent successfully!")
