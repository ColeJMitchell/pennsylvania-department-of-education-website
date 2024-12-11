import pandas as pd
from django.core.management.base import BaseCommand
from pages.models import School, SchoolFiscal

class Command(BaseCommand):
    help = 'Import fiscal data from CSV into the database'

    def handle(self, *args, **kwargs):
        self.add_data()

    def add_data(self):
        csv_file_path = r'C:\Users\jad54\Desktop\cs320\pennsylvania-department-of-education-app\relation_data\school_fiscal_data\school_fiscal_merged.csv'

        try:
            # Read the CSV file into a DataFrame
            df = pd.read_csv(csv_file_path)

            # Rename columns to match the model
            df.rename(columns={
                'SchoolName': 'school_name',
                'AcademicYearId': 'year',
                'Federal-Non-Personnel': 'federal_non_personnel',
                'Federal-Personnel': 'federal_personnel',
                'Local-Non-Personnel': 'local_non_personnel',
                'Local-Personnel': 'local_personnel',
                'State-Non-Personnel': 'state_non_personnel',
                'State-Personnel': 'state_personnel'
            }, inplace=True)

            for _, row in df.iterrows():
                school_name = row['school_name'].strip().lower()
                schools = School.objects.filter(name__iexact=school_name)

                if schools.count() == 1:
                    school = schools.first()  # Single match found
                elif schools.count() > 1:
                    self.stdout.write(self.style.WARNING(f"Multiple schools found for '{school_name}'. Skipping this record."))
                    continue
                else:
                    self.stdout.write(self.style.ERROR(f"School '{school_name}' not found in the database."))
                    continue

                # Create a new SchoolFiscal record
                fiscal_record = SchoolFiscal(
                    school_id=school,
                    year=row['year'],
                    federal_non_personnel=row['federal_non_personnel'],
                    federal_personnel=row['federal_personnel'],
                    local_non_personnel=row['local_non_personnel'],
                    local_personnel=row['local_personnel'],
                    state_non_personnel=row['state_non_personnel'],
                    state_personnel=row['state_personnel']
                )
                fiscal_record.save()
                self.stdout.write(self.style.SUCCESS(f"Added fiscal record for school: {school_name}, year: {row['year']}"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred while importing data: {e}"))
