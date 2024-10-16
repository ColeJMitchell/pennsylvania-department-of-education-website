import os
import django
import csv

# Set up the Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webdatabase.settings')
django.setup()

from pages.models import enrollment

def add_data():
    # Open the CSV file for reading
    with open("Enrollment_Data.csv", mode="r") as f:
        reader = csv.reader(f)

        for row in reader:
            enrollment.objects.create(
                district=row[0],
                school=row[1],
                enrollmentnum=int(row[2]),  
                years=row[3]
            )

if __name__ == "__main__":
    add_data()
