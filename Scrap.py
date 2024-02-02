from bs4 import BeautifulSoup
import requests
import io
import sys
import time



my_bot_token = '6924733624:AAFHAlNXqgbb7Ya6ckREg9cRh2JH1nsSVyM'
chat_id = '562966669'

response = requests.get('https://jiji.com.et/search?query=Iphone')
soup = BeautifulSoup(response.text, 'html.parser')
IphoneTypes = soup.find_all('div', class_='b-advert-title-inner qa-advert-title b-advert-title-inner--div')
description = soup.find_all('div', class_='b-list-advert-base__description-text')
links = soup.find_all('div', class_='b-list-advert__gallery__item js-advert-list-item')

def send_to_telegram(my_bot_token, chat_id, text):
    url = f"https://api.telegram.org/bot{my_bot_token}/sendMessage"
    params = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.post(url, params=params)
    return response.json()

for index, entry in enumerate(IphoneTypes):
    Name = entry.get_text(strip=True)
    Phonedescription = description[index].get_text(strip=True)
    
    link = links[index].find('a', href=True)['href']
    
    texts = f"Iphone-Model:- {Name}\n Phone Details: {Phonedescription}\n The link: {'https://jiji.com.et' + link}\n"
    response = send_to_telegram(my_bot_token, chat_id, texts)
    print(response)
    time.sleep(1)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')