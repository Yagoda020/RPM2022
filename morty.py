import json
import requests

data = {}
for i in range(10, 13):
    res = requests.get(f"https://rickandmortyapi.com/api/character/?page={i}")
    for person in list(res.json()['results']):         
        data[person['id']] = {person['name']: person['type']}

json_string = json.dumps(data)
with open('morty.json', 'w') as outfile:
    json.dump(json_string, outfile)