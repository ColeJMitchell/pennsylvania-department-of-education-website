import pandas as pd
from django.core.management.base import BaseCommand
from pages.models import School, SchoolKeystone

class Command(BaseCommand):
   help = 'Import Keystone exam data from CSV into the database'

   def handle(self, *args, **kwargs):
      self.add_data()

   def add_data(self):
      csv_file_path = r'C:\Users\jad54\Desktop\cs320\pennsylvania-department-of-education-app\relation_data\school_keystone_data\merged_keystone_exam_data_2015_2023.csv'

      try:
         # Read the CSV file into a DataFrame
         df = pd.read_csv(csv_file_path)

         # Rename columns to match the model
         df.rename(columns={
            'School Name': 'school_name',
            'Subject': 'subject',
            'Group': 'group',
            'Number Scored': 'numbers_scored',
            'Percent Advanced': 'percent_advanced',
            'Percent Proficient': 'percent_proficient',
            'Percent Basic': 'percent_basic',
            'Percent Below Basic': 'percent_below_basic'
         }, inplace=True)

         for _, row in df.iterrows():
            school_name = row['school_name'].strip().lower()
            schools = School.objects.filter(name__iexact=school_name)

            if schools.count() == 1:
               school = schools.first()  # Get the single matching, IDEAL
            elif schools.count() > 1:
               self.stdout.write(self.style.WARNING(f"Multiple schools found for '{school_name}'. Skipping this record.")) # This happened so, we got some dups
               continue
            else:
               self.stdout.write(self.style.ERROR(f"School '{school_name}' not found in the database."))
               continue

            # Create new record
            keystone_record = SchoolKeystone(
               school_id=school,
               year=row['Year'],
               subject=row['subject'],
               group=row['group'],
               numbers_scored=int(row['numbers_scored']) if str(row['numbers_scored']).isdigit() else 0,
               percent_advanced=float(row['percent_advanced']) if str(row['percent_advanced']).replace('.', '', 1).isdigit() else -1,
               percent_proficient=float(row['percent_proficient']) if str(row['percent_proficient']).replace('.', '', 1).isdigit() else -1,
               percent_basic=float(row['percent_basic']) if str(row['percent_basic']).replace('.', '', 1).isdigit() else -1,
               percent_below_basic=float(row['percent_below_basic']) if str(row['percent_below_basic']).replace('.', '', 1).isdigit() else -1
            )
            keystone_record.save()
            self.stdout.write(self.style.SUCCESS(f"Added Keystone record for school: {school_name}, year: {row['Year']}"))

      except Exception as e:
         self.stdout.write(self.style.ERROR(f"An error occurred while importing data: {e}"))
