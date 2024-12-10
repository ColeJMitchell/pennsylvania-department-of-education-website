import os
import django
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webdatabase.settings')
django.setup()

from pages.models import School

csv_file_path = ("/home/lasha/github/pennsylvania-department-of-education-app/relation_data/schools_data"
                 "/locations.csv")

with open(csv_file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # skip header

    for row in csv_reader:
        school_name = row[0].strip()
        latitude = float(row[1])
        longitude = float(row[2])

        schools = School.objects.filter(name=school_name)
        if schools.count() == 1:
            school = schools.first()
            school.latitude = latitude
            school.longitude = longitude
            school.save()
            print(f"Updated {school.name} with latitude {latitude} and longitude {longitude}")
        else:
            print(f"Multiple schools found for {school_name}. Skipping update.")

print("Latitude and longitude update completed.")