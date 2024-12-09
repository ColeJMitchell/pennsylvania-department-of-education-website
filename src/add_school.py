import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webdatabase.settings')
django.setup()

from pages.models import School, district

print(School.objects.count())  # Verify the total number of schools added
# Check if data is linked to districts
# check district_id = 1  school names
print(School.objects.filter(district_id=1).values_list('name', flat=True))

# import os
# import django
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webdatabase.settings')
# django.setup()
#
# import csv
# from pages.models import School, district
#
# csv_file_path = ("/home/lasha/github/pennsylvania-department-of-education-app/relation_data/schools_data"
#                  "/schools_modified.csv")
#
# # creating a dictionary of district names and IDs. This will be used to get the district ID for each school
# # because the school data only contains the district name. The district_name also needs to be stripped of any
# # leading or trailing whitespace and converted to lowercase to match the district names in the database.
# district_dict = {dist.district_name.strip().lower(): dist.district_id for dist in district.objects.all()}
#
# # Read the CSV and add data to the School model
# with open(csv_file_path, mode='r') as file:
#     csv_reader = csv.reader(file)
#     next(csv_reader)  # skip header
#
#     for row in csv_reader:
#         district_name = row[0].strip().lower()
#
#         if district_name in district_dict:
#             district_id = district_dict[district_name]
#         else:
#             # If the district name is not found in the dictionary, set district_id to -1
#             district_id = -1
#
#         new_school = School(
#             district_id=district_id,  # FK to the district model
#             name=row[1],  # School name
#             address_city=row[2],
#             address_street=row[3],
#             county=row[4],
#             zip=row[5],
#             telephone=row[6],
#             website=row[7],
#             elementary=row[8].lower() == "true",  # Convert string to boolean
#             middle=row[9].lower() == "true",
#             high=row[10].lower() == "true"
#         )
#         new_school.save()
#
# print("School data has been successfully added to the database.")

# Code to verify the data has been added to the database

# import os
# import django
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webdatabase.settings')
# django.setup()
#
# from pages.models import School
#
# # Query all schools
# schools = School.objects.all()
#
# # Print each school's details
# for school in schools:
#     print(f"School Name: {school.name}, District ID: {school.district_id}, Address: {school.address_street}, {school.address_city}, {school.zip}, County: {school.county}, Telephone: {school.telephone}, Website: {school.website}, Elementary: {school.elementary}, Middle: {school.middle}, High: {school.high}")

