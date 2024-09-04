import requests
from bs4 import BeautifulSoup
import os

# Check if the tag is a link to a data file (futurereadypa.org)
def is_datafile_link_futurereadypa(tag):
    return tag.name == 'a' and tag.get('href') and tag['href'].startswith('/home/getdatafile?')

# Check if the tag is a link to a data file (education.pa.gov)
def is_datafile_link_educationpa(tag):
    return tag.name == 'a' and tag.get('href') and tag['href'].endswith('.xlsx')

# Download data files
def download_datafiles(base_url, url_list, output_folder, is_datafile_link):
    
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
                filename = data.text.replace(' ', '_').replace(':', '') + '.xlsx'
                with open(os.path.join(output_folder, filename), 'wb') as f:
                    f.write(link_response.content)
        # Handle invalid URLs
        except requests.exceptions.MissingSchema:
            print(f"Invalid URL: {url}")

# Change the working directory to the application folder
os.chdir("pennsylvania-department-of-education-app")

# Below numbers correspond to the data sources on Assignment Description Page

# 1 - 5 (futurereadypa.org)
download_datafiles("https://futurereadypa.org", ["/Home/DataFiles"], "data", is_datafile_link_futurereadypa)

# 6 - 9, 11 - 15, 17 (education.pa.gov)
education_pa_urls = ["/DataAndReporting/LoanCanLowIncome/Pages/PublicSchools.aspx", "/DataAndReporting/LoanCanLowIncome/Pages/PrivateSchools.aspx", "/DataAndReporting/Assessments/Pages/Keystone-Exams-Results.aspx", "/DataAndReporting/Assessments/Pages/PSSA-Results.aspx", "/DataAndReporting/Graduates/Pages/default.aspx", "/DataAndReporting/Dropouts/Pages/default.aspx", "/DataAndReporting/CohortGradRate/Pages/default.aspx", "/DataAndReporting/Enrollment/Pages/PublicSchEnrReports.aspx", "/DataAndReporting/Enrollment/Pages/PrivateNPEnrRpts.aspx", "/DataAndReporting/ProfSupPers/Pages/ProfStaffSummary.aspx"]
download_datafiles("https://www.education.pa.gov", education_pa_urls, "data", is_datafile_link_educationpa)

# currently missing 10 and 16