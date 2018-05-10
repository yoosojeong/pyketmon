import requests
from bs4 import BeautifulSoup

all_monster = []

req = requests.get('http://ko.pokemon.wikia.com/wiki/%EC%A0%84%EA%B5%AD%EB%8F%84%EA%B0%90')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
my_titles = soup.select(
    'td > a'
    )

for title in my_titles:
    if not title.text is  '':
        all_monster.append(title.text)

print(all_monster)