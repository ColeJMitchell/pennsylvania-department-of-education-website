import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webdatabase.settings')
django.setup()

from pages.models import enrollment

def delete_all_enrollments():
    enrollment.objects.all().delete()

if __name__ == "__main__":
    delete_all_enrollments()
