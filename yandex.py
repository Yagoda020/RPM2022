import requests
# from bs4 import BeautifulSoup

# HOST = 'https://music.yandex.ru/'
# URL = 'https://music.yandex.ru/chart'
# HEADERS = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'user-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
# }

# cookies = {
#     'yandexuid': '9512048811638873542',
#     'yuidss': '9512048811638873542',
#     'is_gdpr': '0',
#     'is_gdpr_b': 'COHeURCdVSgC',
#     'ymex': '1954233569.yrts.1638873569',
#     'gdpr': '0',
#     '_ym_uid': '1638873569361653969',
#     'my': 'YwA=',
#     'amcuid': '2904986791649196613',
#     'mda': '0',
#     'yandex_gid': '75',
#     '_ym_d': '1661088521',
#     'yabs-frequency': '/5/0G000EQKq6800000/LVTwO9j8Vb8SI25lfLmS6hB2Qnn89wfttSJEUurM74Z0/',
#     'skid': '4282033431661095796',
#     'yp': '1978111191.udn.cDp3d3dXMTIzMzM%3D#1958751994.multib.1#1663680521.ygu.1#1673242226.szm.2:1180x820:1123x716#1661090321.rnwcst.1#1663766936.csc.1',
#     'L': 'Bwh2UX19Q1p6U35FXGZPAmcFVWZ2BX9UBUNPOVpVYQRK.1662751191.15095.350315.6d002bb86a1f985f3e5f3b8fcccbca43',
#     'yandex_login': 'wwwW12333',
#     'i': 'yLA40dvCEnacIJUBuk2BRQy37wgD3Wdjnrt7xPBFuWyYiHOONHRp6o3jv+KHe4Zb0W+WoziR4aMLfwcDPfyUkcU3ECk=',
#     'Session_id': '3:1663066096.5.3.1638873712797:v6OivA:2b.1.2:1|1427890893.0.2.0:3|1473107788.4518282.2.0:3.2:4518282|793936790.10095200.2.2:10095200|1066790460.-1.2.1:236683642.2:10095534|1619483060.11997697.2.2:11997697|1660813492.18963131.2.2:18963131|3:10258183.954407.k59zbOEyWsnlkb2Xt0AztHWpbsY',
#     'sessionid2': '3:1663066096.5.3.1638873712797:v6OivA:2b.1.2:1.499:1|1427890893.0.2.0:3|1473107788.4518282.2.0:3.2:4518282|793936790.10095200.2.2:10095200|1066790460.-1.2.1:236683642.2:10095534|1619483060.11997697.2.2:11997697|1660813492.18963131.2.2:18963131|3:10258183.515183.fakesign0000000000000000000',
#     'ys': 'udn.cDp3d3dXMTIzMzM%3D#c_chck.3213401720',
#     '_ym_isad': '2',
#     'chromecast': '\'\'',
#     'device_id': 'afb1ea901e77f7877fe42dc7c500e60019e8e302e',
#     'lastVisitedPage': '%7B%7D',
#     'active-browser-timestamp': '1663068044449',
#     '_yasc': 'tx143Ts7Ef9r68R8Mu2Bp/7zpRw71F6xvjUudu1NZxUmAzfi9tMtMw==',
# }

# headers = {
#     'Accept': 'application/json, text/javascript, */*; q=0.01',
#     'Accept-Language': 'en-US,en;q=0.9',
#     'Connection': 'keep-alive',
#     # Requests sorts cookies= alphabetically
#     # 'Cookie': 'yandexuid=9512048811638873542; yuidss=9512048811638873542; is_gdpr=0; is_gdpr_b=COHeURCdVSgC; ymex=1954233569.yrts.1638873569; gdpr=0; _ym_uid=1638873569361653969; my=YwA=; amcuid=2904986791649196613; mda=0; yandex_gid=75; _ym_d=1661088521; yabs-frequency=/5/0G000EQKq6800000/LVTwO9j8Vb8SI25lfLmS6hB2Qnn89wfttSJEUurM74Z0/; skid=4282033431661095796; yp=1978111191.udn.cDp3d3dXMTIzMzM%3D#1958751994.multib.1#1663680521.ygu.1#1673242226.szm.2:1180x820:1123x716#1661090321.rnwcst.1#1663766936.csc.1; L=Bwh2UX19Q1p6U35FXGZPAmcFVWZ2BX9UBUNPOVpVYQRK.1662751191.15095.350315.6d002bb86a1f985f3e5f3b8fcccbca43; yandex_login=wwwW12333; i=yLA40dvCEnacIJUBuk2BRQy37wgD3Wdjnrt7xPBFuWyYiHOONHRp6o3jv+KHe4Zb0W+WoziR4aMLfwcDPfyUkcU3ECk=; Session_id=3:1663066096.5.3.1638873712797:v6OivA:2b.1.2:1|1427890893.0.2.0:3|1473107788.4518282.2.0:3.2:4518282|793936790.10095200.2.2:10095200|1066790460.-1.2.1:236683642.2:10095534|1619483060.11997697.2.2:11997697|1660813492.18963131.2.2:18963131|3:10258183.954407.k59zbOEyWsnlkb2Xt0AztHWpbsY; sessionid2=3:1663066096.5.3.1638873712797:v6OivA:2b.1.2:1.499:1|1427890893.0.2.0:3|1473107788.4518282.2.0:3.2:4518282|793936790.10095200.2.2:10095200|1066790460.-1.2.1:236683642.2:10095534|1619483060.11997697.2.2:11997697|1660813492.18963131.2.2:18963131|3:10258183.515183.fakesign0000000000000000000; ys=udn.cDp3d3dXMTIzMzM%3D#c_chck.3213401720; _ym_isad=2; chromecast=\'\'; device_id=afb1ea901e77f7877fe42dc7c500e60019e8e302e; lastVisitedPage=%7B%7D; active-browser-timestamp=1663068044449; _yasc=tx143Ts7Ef9r68R8Mu2Bp/7zpRw71F6xvjUudu1NZxUmAzfi9tMtMw==',
#     'Referer': 'https://music.yandex.ru/chart',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-origin',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
#     'X-Current-UID': '1066790460',
#     'X-Requested-With': 'XMLHttpRequest',
#     'X-Retpath-Y': 'https://music.yandex.ru/chart',
#     'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"macOS"',
# }

# params = {
#     'what': 'chart',
#     'lang': 'ru',
#     'external-domain': 'music.yandex.ru',
#     'overembed': 'false',
#     'ncrnd': '0.35068374359424204',
# }

# response = requests.get('https://music.yandex.ru/handlers/main.jsx', params=params, cookies=cookies, headers=headers)

# def get_html(url, params=''):
#     r = requests.get(url, headers=HEADERS, params=params)
#     return r

# def get_content(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     items = soup.find_all('div', class_='d-track')
#     chartPosition = soup.find_all('div', class_='d-track__chart-number typo deco-typo')
#     print(chartPosition)
#     cards = []
   
#     for item in items:
#         cards.append(
#             {
#                 'name':item.find('div', class_='d-track__chart').get_text(strip=True),
#                 'artists':item.find('div', class_='d-track__meta').get_text(strip=True),
#                 'link_product':HOST + item.find('div', class_='d-track__name').find('a').get('href')
#             }
#         )
#     return cards

# html = get_html(URL)
# print(get_content(html.text))

# def parser(URL_TEMPLATE):
#     r = requests.get(URL_TEMPLATE)
#     jsonData = r.json()
#     for json in jsonData['chartPositions']:
#         pos = json['chartPosition']['position']
#         print(pos)

# parser('https://music.yandex.ru/handlers/main.jsx?what=chart&lang=ru&external-domain=music.yandex.ru&overembed=false')

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

print(goParse())