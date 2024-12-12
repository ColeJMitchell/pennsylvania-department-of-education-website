import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webdatabase.settings')
django.setup()
from pages.models import districtFiscal, district
import csv

# Adds the district keystone data to the database from the cleaned csv files
for yearval in (2016, 2017, 2018, 2021):
    with open(f"/home/lasha/github/pennsylvania-department-of-education-app/relation_data/district_fiscal_data/district_fiscal_{yearval}.csv", mode='r') as file:
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
                federal_revenue = float(row[1])
                local_revenue = float(row[2])
                state_revenue = float(row[3])
                total_expenditures = float(row[4])
                total_revenue = float(row[5])
                year = int(row[6])

                new_district_fiscal = districtFiscal(
                    district_id=district_instance,
                    federal_revenue = federal_revenue,
                    local_revenue = local_revenue,
                    state_revenue = state_revenue,
                    total_expenditures = total_expenditures,
                    total_revenue = total_revenue,
                    year=year
                )

                new_district_fiscal.save()
                print(f"Saved districtKeystone for district: {district_instance.district_name}, Year: {year}")

            except ValueError as e:
                print(f"Error converting data for district '{row[0]}': {e}")
                continue
