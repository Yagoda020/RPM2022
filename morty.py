import json
import requests

data = {}
for i in range(10, 13):
    res = requests.get(f"https://rickandmortyapi.com/api/character/?page={i}")
    for person in list(res.json()['results']):         
        data[person['id']] = {person['name']: {person['url']: person['type']}}

with open('morty.json', 'w') as outfile:
    json.dump(data, outfile,indent=4)
