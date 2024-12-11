from django.core.management.base import BaseCommand
from pages.models import SchoolFiscal

class Command(BaseCommand):
    help = 'Delete all school fiscal records from the database'

    def handle(self, *args, **kwargs):
        self.delete_all_school_keystone()

    def delete_all_school_keystone(self):
        count, _ = SchoolFiscal.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'Deleted {count} school fiscal records.'))