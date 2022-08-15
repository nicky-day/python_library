import json

with open("myinfo.json") as f:
    data = json.load(f)


type(data)
data


data = {"name": "홍길동", "birth": "0525", "age": 30}
with open("myinfo.json", "w") as f:
    json.dump(f)


d = {"name": "홍길동", "birth": "0525", "age": 30}
json_data = json.dumps(d)
json_data
json.loads(json_data)

json_data = json.dumps(d, ensure_ascii=False)
json_data
json.loads(json_data)

print(json.dumps(d, indent=2, ensure_ascii=2))

json.dumps([1, 2, 3])
json.dumps((4, 5, 6))
