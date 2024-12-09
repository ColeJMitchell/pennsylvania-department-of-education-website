import os
import django
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webdatabase.settings')
django.setup()
#
# from pages.models import School, SchoolGraduation
#
# # Query all school names from the School model and create a dictionary
# school_names_db_dict = {name.strip().lower(): school for name, school in School.objects.values_list('name', 'school_id')}
#
# def parse_float(value, default=0.0):
#     try:
#         return float(value)
#     except (ValueError, TypeError):
#         return default
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
#                 school = school_names_db_dict[school_name]
#                 new_enrollment = SchoolGraduation(
#                     school_id=school,
#                     year=year,
#                     graduation_count=int(row[1]),
#                     college_bound=int(row[2]),
#                     two_or_four_year_college_or_university=int(row[3]),
#                     total_postsecondary_bound=int(row[4]),
#                     non_degree_granting_postsecondary_bound=int(row[5]),
#                     specialized_associates_degree_granting_institution=int(row[6])
#                 )
#
#                 new_enrollment.save()
#             else:
#                 count += 1
#
#     print(f"Data for the year {year}-{year + 1} has been successfully added to the database.")
#     print(f"Number of schools not found in the database: {count}")
#
# print("School data has been successfully added to the database.")



