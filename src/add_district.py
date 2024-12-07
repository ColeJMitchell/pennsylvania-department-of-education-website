import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webdatabase.settings')
django.setup()
from pages.models import district
import csv

with open('/home/cole/github/pennsylvania-department-of-education-app/relation_data/district_data/cleaned_district.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        csv_reader = csv.reader(file) 
        for row in csv_reader:
            new_district = district(
                district_name=row[0],
                district_address_city=row[1],
                district_address_street=row[2],
                district_zip_code=row[3],
                geographic_size_square_miles=row[4]
            )
            new_district.save()