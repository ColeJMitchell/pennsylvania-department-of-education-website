import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webdatabase.settings')
django.setup()

from pages.models import districtKeystone

# Delete all records in the district table
districtKeystone.objects.all().delete()

print("All records in the district table have been deleted.")
