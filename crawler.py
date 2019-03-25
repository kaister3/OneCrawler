from bs4 import BeautifulSoup
import requests


print('获取格言信息..')
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    }
user_url = 'http://wufazhuce.com/'
resp = requests.get(user_url, headers=headers)
soup_texts = BeautifulSoup(resp.text, 'lxml')
every_msg = soup_texts.find_all('div', class_='fp-one-cita')[0].find('a').text
print(every_msg)