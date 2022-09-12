import requests
import pprint

url = "https://jsonplaceholder.typicode.com/posts/1"
res = requests.get(url)
print(res.json)
pprint.pprint(res.json())


def get_wikidocs(page):
    url = "https://wikidocs.net/{}".format(page)
    res = requests.get(url)
    with open("wikidocs_%s.html" % page, "w", encoding="utf-8") as f:
        f.write(res.text)


get_wikidocs(2)
