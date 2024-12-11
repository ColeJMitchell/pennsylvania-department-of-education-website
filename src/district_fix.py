import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webdatabase.settings')
django.setup()

from pages.models import district, School
#
# for s in School.objects.all():
#     try:
#         d = district.objects.get(district_id=s.district_id)
#         s.district_fk = d
#         s.save()
#     except district.DoesNotExist:
#         # Handle case where there's no matching district, if needed.
#         pass


schools = School.objects.all()
for entry in schools:
    print(f"School Name: {entry.name},District_id: {entry.district_id}")