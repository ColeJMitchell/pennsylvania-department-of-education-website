from django.core.management.base import BaseCommand
from pages.models import SchoolKeystone 

class Command(BaseCommand):
    help = 'Delete all school keystone records from the database'

    def handle(self, *args, **kwargs):
        self.delete_all_school_keystone()

    def delete_all_school_keystone(self):
        count, _ = SchoolKeystone.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'Deleted {count} enrollment records.'))