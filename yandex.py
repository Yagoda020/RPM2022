import requests

def goParse():
    r = requests.get('https://music.yandex.ru/handlers/main.jsx?what=chart&lang=ru&external-domain=music.yandex.ru&overembed=false')
    finish = {   
    }
    artistName = [
    ]
    
    jsonData = r.json()['chartPositions']

    for js in jsonData:
        for art in js['track']['position']:
            artistName.append(art['name'])
            chartPos = js['chartPosition']['position']
            trackName = js['track']['title']

            finish[chartPos] = {
                'name': trackName,
                'artists': artistName
            }
    
    return finish

if __name__ == '__main__':
    with open('js.json', 'w') as file:
        json.dump(goParse(), file)
