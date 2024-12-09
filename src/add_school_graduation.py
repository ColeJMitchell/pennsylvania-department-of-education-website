import os
import django
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webdatabase.settings')
django.setup()

from pages.models import School, SchoolGraduation

# # Query all school names from the School model and create a dictionary
# school_names_db_dict = {name.strip().lower(): school_id for name, school_id in School.objects.values_list('name', 'school_id')}
# # parse int
# def parse_int(value, default=0):
#     try:
#         return int(value)
#     except (ValueError, TypeError):
#         return default
#
#
# for year in range(2016, 2023):
#     count = 0
#     csv_file_path = f"/home/lasha/github/pennsylvania-department-of-education-app/relation_data/school_graduation_data/{year}-{year + 1}.csv"
#
#     with open(csv_file_path, mode='r') as file:
#         csv_reader = csv.reader(file)
#         header = next(csv_reader)  # Skip the header row
#
#         for row in csv_reader:
#             school_name = row[0].strip().lower()
#             if school_name in school_names_db_dict:
#                 school = School.objects.get(school_id=school_names_db_dict[school_name])  # Retrieve School instance
#                 new_graduation = SchoolGraduation(
#                     school_id=school,
#                     year=year,
#                     graduation_count= parse_int(row[1]),
#                     college_bound= parse_int(row[2]),
#                     two_or_four_year_college_or_university=parse_int(row[3]),
#                     total_postsecondary_bound= parse_int(row[4]),
#                     non_degree_granting_postsecondary_bound= parse_int(row[5]),
#                     specialized_associates_degree_granting_institution= parse_int(row[6])
#                 )
#                 new_graduation.save()
#             else:
#                 count += 1
#
#     print(f"Data for the year {year}-{year + 1} has been successfully added to the database.")
#     print(f"Number of schools not found in the database: {count}")
#
# print("School data has been successfully added to the database.")

# print each entry in the SchoolGraduation model
count = 0
for entry in SchoolGraduation.objects.all():

    print(entry.school_id, entry.year, entry.graduation_count, entry.college_bound, entry.two_or_four_year_college_or_university, entry.total_postsecondary_bound, entry.non_degree_granting_postsecondary_bound, entry.specialized_associates_degree_granting_institution)
    count += 1

print(f"Total number of entries: {count}")


