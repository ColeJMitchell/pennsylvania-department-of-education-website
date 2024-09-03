import requests
from bs4 import BeautifulSoup

url_list = ["https://futurereadypa.org/Home/DataFiles", ""]

for url in url_list:
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        data_blocks = soup.find_all(lambda tag: tag.name == 'a' and tag.get('href') and tag['href'].startswith('/home/getdatafile?'))
        for data in data_blocks:
            print(data)
    except requests.exceptions.MissingSchema:
        print(f"Invalid URL: {url}")
    