import requests
import pprint

url = "https://jsonplaceholer.typicode.com/posts/1"
res = requests.delete(url)
pprint.pprint(res.json())
