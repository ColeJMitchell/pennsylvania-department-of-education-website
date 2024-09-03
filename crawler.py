import requests
from bs4 import BeautifulSoup

url_list = ["https://futurereadypa.org/Home/DataFiles"]

for url in url_list:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    data_blocks = soup.find_all("td")
    for data in data_blocks:
        print(data)
    
