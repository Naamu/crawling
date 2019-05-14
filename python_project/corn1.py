import requests
from bs4 import BeautifulSoup
import telegram

def 네이버_실검():
    res = requests.get("http://naver.com")
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    tag_list = soup.select('.PM_CL_realtimeKeyword_rolling .ah_k')

    keyword_list = []

    for tag in tag_list:
        label = tag.text
        keyword_list.append(label)

    return keyword_list


chat_id = '-306435043'
#https://api.telegram.org/bot838565849:AAG9DuCy2saTeIpFrkpr2N1NB9mtLGRj1NE/getUpdates 에서 chat_id 확인
TOKEN = '838565849:AAG9DuCy2saTeIpFrkpr2N1NB9mtLGRj1NE'

text = '\n'.join(네이버_실검())

bot = telegram.Bot(token = TOKEN)
bot.send_message(chat_id=chat_id, text=text)
