import requests
from bs4 import BeautifulSoup
import os

output_folder = "data"
base_url = "https://futurereadypa.org"
url_list = ["/Home/DataFiles"]

# Check if the tag is a link to a data file
def is_datafile_link(tag):
    return tag.name == 'a' and tag.get('href') and tag['href'].startswith('/home/getdatafile?')

# Change the working directory to the app folder
os.chdir('pennsylvania-department-of-education-app')

# Check if the output folder exists, if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for url in url_list:
    try:
        full_url = base_url + url
        response = requests.get(full_url)
        soup = BeautifulSoup(response.content, "html.parser")
        data_blocks = soup.find_all(is_datafile_link)
        
        # Loop through all the links and download the data files
        for i, data in enumerate(data_blocks):
            link = data['href']
            link_url = base_url + link
            link_response = requests.get(link_url)
            filename = data.text.replace(' ', '_') + '.xlsx'
            with open(os.path.join(output_folder, filename), 'wb') as f:
                f.write(link_response.content)
    # Handle invalid URLs
    except requests.exceptions.MissingSchema:
        print(f"Invalid URL: {url}")
    