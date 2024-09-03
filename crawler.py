import requests
from bs4 import BeautifulSoup

url_list = []

for url in url_list:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    data_blocks = soup.find_all('a')
    