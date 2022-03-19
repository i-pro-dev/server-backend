import selenide
import urllib3
import requests
from lxml import etree
from bs4 import BeautifulSoup

def search(name : str, search_engine : str) -> list:
    """
    На вход:
        name - "Имя Фамилия"
        search_engine - "Пока что яндекс онли"
    Возвращает куски html с упоминанием Имя Фамилия на первой странице
    """
    res : list = []
    user_agent = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) ..'}
    http = urllib3.PoolManager(headers = user_agent)

    # Yandex only
    # req = http.request('GET', f"https://{search_engine}/search/?text={'+'.join(name.split(' '))}")
    req = requests.get(f"https://{search_engine}/search/?text={'+'.join(name.split(' '))}", headers=user_agent)

    # soup = BeautifulSoup(req.data, 'html.parser')

    # TODO: Issue - shadow throttle? No result on second attempt

    soup = BeautifulSoup(req.content, 'html.parser')
    dom = etree.HTML(str(soup))
    res = dom.xpath('//*[contains(@class,"serp-item")]')
    with open("search_result.html", 'w') as f:
        for r in res:
            print(r.text)
            f.write(r.text)
    return res


if __name__=="__main__":
    name : str = "Егор Смурыгин"
    search(name, "yandex.ru")
