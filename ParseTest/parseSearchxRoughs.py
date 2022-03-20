import requests
import json

def search(name: str, search_engine: str) -> list:
    """
    На вход:
        name - "Имя Фамилия"
        search_engine - "Пока что search_engine онли"
    Возвращает куски html с упоминанием Имя Фамилия на первой странице
    """
    res: list = []
    #user_agent = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) ..'}
    #http = urllib3.PoolManager(headers=user_agent)
    #req = http.request(
    #    'GET',
    req = requests.get(
    f"https://{search_engine}/search",
        params = {
            "q": name,
            "format": "json",
            "safesearch" : 1,
            "categories" : "news"
        })
    d = json.loads(req.text)
    #with open("res.txt", "w") as f:
    #    f.write(str(json.loads(req.text)))

    res = [(site["title"], site["content"], site["url"]) for site in d["results"]]
    return res


if __name__ == "__main__":
    name: str = "Ваник Манукян"
    res = search(name, "searx.roughs.ru")
    _ = [print(r[0]) for r in res]
