from django.core.management.base import BaseCommand
from pages.models import enrollment 

class Command(BaseCommand):
    help = 'Delete all enrollment records from the database'

    def handle(self, *args, **kwargs):
        self.delete_all_enrollments()

    def delete_all_enrollments(self):
        count, _ = enrollment.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'Deleted {count} enrollment records.'))
