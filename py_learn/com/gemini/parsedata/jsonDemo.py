import json

# python转JSON
data = {
    "no": 1,
    "name": "鼓泡",
    "url": "https://www.gupao.com",
    None: True
}
json_str = json.dumps(data)
print(type(json_str))
print(data)
print(json_str)

str = json.loads(json_str)
print(str)
print(type(str))
file = open("data.json","w")
file.write(data,file)

with open("data", "w") as f:
    json.dump(data, f)

with open("data.json","r") as f:
    data1 = json.load(f)
print(data1)