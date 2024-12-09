import os
import django
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webdatabase.settings')
django.setup()

from pages.models import School, SchoolEnrollment
#
#
# # Query all school names from the School model
# school_names_db = set(School.objects.values_list('name', flat=True))
#
# # create a dictionary of school names that are filtered and stripped of any leading or trailing whitespace and converted to
# # lowercase. each name is mapped to the id in the database.
# school_names_db_dict = {name.strip().lower(): id for name, id in School.objects.values_list('name', 'school_id')}
#
# def parse_float(value, default=0.0):
#     try:
#         return float(value)
#     except (ValueError, TypeError):
#         return default
#
# for year in range(2022, 2024):
#     count = 0
#     csv_file_path = f"/home/lasha/github/pennsylvania-department-of-education-app/relation_data/school_enrollment_data/{year}-{year + 1}.csv"
#     with open(csv_file_path, mode='r') as file:
#         csv_reader = csv.reader(file)
#         header = next(csv_reader)  # Skip the header row
#
#         for row in csv_reader:
#             school_name = row[0].strip().lower()
#             if school_name in school_names_db_dict:
#                 school_id = school_names_db_dict[school_name]
#                 new_enrollment = SchoolEnrollment(
#                     school_id_id=school_id,
#                     year=year,
#                     two_or_more_races_percent=parse_float(row[1]),
#                     american_indian_alaska_native_percent=parse_float(row[2]),
#                     asian_percent=parse_float(row[3]),
#                     black_african_american_percent=parse_float(row[4]),
#                     hispanic_percent=parse_float(row[5]),
#                     homeless_percent= parse_float(row[6]),
#                     military_connected_percent=parse_float(row[7]),
#                     native_hawaiian_or_pacific_islander_percent=parse_float(row[8]),
#                     percent_of_gifed_students=parse_float(row[9]),
#                     economically_disadvantaged_percent=parse_float(row[10]),
#                     english_learner_percent=parse_float(row[11]),
#                     school_enrollment=int(row[13]) if row[13].isdigit() else 0,
#                     special_education_percent=parse_float(row[14]),
#                     title_i_school=row[15].strip().lower() == 'yes',
#                     white_percent=parse_float(row[16]),
#                 )
#
#                 new_enrollment.save()
#             else:
#                 count += 1
#
#
#     print(f"School enrollment data for {year}-{year + 1} has been successfully added to the database.")
#     print(f"Number of schools not found in the database: {count}")

# print("School data has been successfully added to the database.")



enrollments = SchoolEnrollment.objects.all()

for enrollment in enrollments:
    print(f"School ID: {enrollment.school_id_id}, Year: {enrollment.year}, "
          f"Two or More Races Percent: {enrollment.two_or_more_races_percent}, "
          f"American Indian/Alaska Native Percent: {enrollment.american_indian_alaska_native_percent}, "
          f"Asian Percent: {enrollment.asian_percent}, "
          f"Black/African American Percent: {enrollment.black_african_american_percent}, "
          f"Hispanic Percent: {enrollment.hispanic_percent}, "
          f"Homeless Percent: {enrollment.homeless_percent}, "
          f"Military Connected Percent: {enrollment.military_connected_percent}, "
          f"Native Hawaiian/Pacific Islander Percent: {enrollment.native_hawaiian_or_pacific_islander_percent}, "
          f"Percent of Gifted Students: {enrollment.percent_of_gifed_students}, "
          f"Economically Disadvantaged Percent: {enrollment.economically_disadvantaged_percent}, "
          f"English Learner Percent: {enrollment.english_learner_percent}, "
          f"School Enrollment: {enrollment.school_enrollment}, "
          f"Special Education Percent: {enrollment.special_education_percent}, "
          f"Title I School: {enrollment.title_i_school}, "
          f"White Percent: {enrollment.white_percent}")