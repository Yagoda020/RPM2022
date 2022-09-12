import requests
import numpy as np

TOKEN = "vk1.a.ZYdyf6zlwRB00NRQb51qfsZqZ4VCfajvUMeNBZSWku_flurF6sOqjtYlZasbaHnTZBU4_o4PfIFAXyS-sM921oSnZ1gpWoqcRFoyoboLYxrkv6qNCvbj7Af7Lh3dfjlr0U44z0E2D0k4VCQEJJSmjsXBJkMwBhP_gmZTDcnoCjLQMj4dnq2nPR2v0NlBkQQR&expires_in=0&user_id=619687273"

def get_average_age ():
    url = f'https://api.vk.com/method/friends.get?fields=bdate&access_token={TOKEN}&v=5.131'
    response = requests.get(url)
    data = response.json()
    list_year = []

    for item in data['response']['items']:
        try:
            data = (item["bdate"])
            
            if len(data) > 2:
                hash = int(data[-4:])
                list_year.append(hash)
                average = np.mean(list_year)
        except: pass
   
    return 2022 - average
            
if __name__ == '__main__':
    average = get_average_age()
    print("Средний возраст равен: ",  average)