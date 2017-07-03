import requests
from bs4 import BeautifulSoup
import os


INIT_PAGE = "http://www.photos-de-trains.net/search.php?type_aff=2&materiel=c11&limit=40&sort=4&page=4"
LABEL = "steam"

data_path = "data/test/"+LABEL+"/"

if not os.path.exists(data_path):
    os.makedirs(data_path)



result = requests.get(INIT_PAGE)
rcontent = result.content
soup = BeautifulSoup(rcontent, "html.parser")
samples = soup.find_all("div", "resultats_r")
for sample in samples:
    hrefphoto = sample.find_all('a', href=True)[0]["href"]
    result = requests.get(hrefphoto)
    rcontent = result.content
    soup = BeautifulSoup(rcontent, "html.parser")
    sample = soup.find_all("div", "little5")
    hrefphoto = sample[0].find_all('a', href=True)[0]["href"]
    print(hrefphoto)
    r = requests.get(hrefphoto, stream=True)
    if r.status_code == 200:
        with open(data_path + hrefphoto.split("/")[-1], 'wb') as f:
            for chunk in r:
                f.write(chunk)