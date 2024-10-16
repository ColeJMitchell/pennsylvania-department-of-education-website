import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webdatabase.settings')
django.setup()
from pages.models import enrollment

def print_enrollment_data():
    enrollment2 = enrollment.objects.all()
    for entry in enrollment2:
        print(f"District: {entry.district}, School: {entry.school}, Enrollment Number: {entry.enrollmentnum}, Years: {entry.years}")

if __name__ == "__main__":
    print_enrollment_data()