import urllib.request
from bs4 import BeautifulSoup

all_map = []

def map():
    html = urllib.request.urlopen('http://ko.pokemon.wikia.com/wiki/%EB%B6%84%EB%A5%98:%EB%A7%B5?display=exhibition&sort=mostvisited')
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.find_all("div", "title")

    for title in titles:
        all_map.append(title.text)

    return all_map
