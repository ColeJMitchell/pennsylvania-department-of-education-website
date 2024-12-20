import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webdatabase.settings')
django.setup()
from pages.models import district, districtKeystone
import csv

for yearval in (2016, 2017, 2018, 2019, 2021, 2022, 2023):
    with open(f"/home/lasha/github/pennsylvania-department-of-education-app/relation_data/district_keystone_data/{yearval}.csv", mode='r') as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            try:
                district_instance = district.objects.get(district_name=row[0])
            except district.DoesNotExist:
                print(f"District '{row[0]}' not found in the database.")
                district_instance = None
                continue
            #makes sure conversion works before addding it to the database
            try:
                numbers_scored = int(row[3])
                percent_advanced = float(row[4])
                percent_proficient = float(row[5])
                percent_basic = float(row[6])
                percent_below_basic = float(row[7])
                # year = int(row[8])

                new_district_keystone = districtKeystone(
                    district_id=district_instance,
                    subject=row[1],
                    group=row[2],
                    numbers_scored=numbers_scored,
                    percent_advanced=percent_advanced,
                    percent_proficient=percent_proficient,
                    percent_basic=percent_basic,
                    percent_below_basic=percent_below_basic,
                    year=yearval
                )

                new_district_keystone.save()
                print(f"Saved districtKeystone for district: {district_instance.district_name}, Year: {yearval}")

            except ValueError as e:
                print(f"Error converting data for district '{row[0]}': {e}")
                continue

    print(f"District Keystone data has been successfully added to the database for year: {yearval}")
