import csv
from django.core.management.base import BaseCommand
from pages.models import enrollment

class Command(BaseCommand):
    help = 'Import enrollment data from CSV into the database'

    def handle(self, *args, **kwargs):
        self.add_data()

    def add_data(self):
        # Open the CSV file for reading
        with open("Enrollment_Data.csv", mode="r") as f: 
            reader = csv.reader(f)

            for row in reader:
                try:
                    enrollment.objects.create(
                        district=row[0],
                        school=row[1],
                        enrollmentnum=int(row[2]),
                        years=row[3]
                    )
                    self.stdout.write(self.style.SUCCESS(f"Added enrollment: {row}"))
                except ValueError as e:
                    self.stdout.write(self.style.ERROR(f"Error adding enrollment from row {row}: {e}"))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Unexpected error: {e}"))
