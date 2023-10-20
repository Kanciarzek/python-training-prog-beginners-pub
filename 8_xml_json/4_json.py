import json

with open("people.json") as file:
    content = json.load(file)  # json.load - przyjmuje dodowny obiekt, na których można wywołać read(), w szczególności plik
    print(content)
print(json.dumps(content, indent=4))

for person in content:
    # print(person["name"])
    print(person["car"])

print(json.loads("{\"name\":\"John\"}"))  # json.loads - przyjmuje obiekt typu str
print(json.dumps({"name": "john"}, indent=4))

