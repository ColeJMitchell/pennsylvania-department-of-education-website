import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webdatabase.settings')
django.setup()
from pages.models import districtKeystone, district, districtFiscal

district2 = districtKeystone.objects.all()
for entry in district2:
    print(f"District: {entry.district_id}, Subject: {entry.subject}, Group: {entry.group}, Numbers Scored: {entry.numbers_scored}, Percent Advanced: {entry.percent_advanced}, Percent Proficient: {entry.percent_proficient}, Percent Basic: {entry.percent_basic}, Percent Below Basic: {entry.percent_below_basic}, Year: {entry.year}")

'''
district3 = district.objects.all()
for entry in district3:
    print(f"District Name: {entry.district_name}, City: {entry.district_address_city}, Street: {entry.district_address_street}, Zip Code: {entry.district_zip_code}, Geographic Size (sq miles): {entry.geographic_size_square_miles}")
'''

'''
district4 = districtFiscal.objects.all()
for entry in district4:
    print(f"District: {entry.district_id}, Federal Revenue: {entry.district_federal_revenue}, Local Revenue: {entry.district_local_revenue}, State Revenue: {entry.district_state_revenue}, Total Expenditures: {entry.district_total_expenditures}, Total Revenue: {entry.district_total_revenue} Year: {entry.year}")
'''