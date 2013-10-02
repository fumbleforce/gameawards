from django.core.management.base import BaseCommand, CommandError
from datetime import date
from runs.models import Run


class Command(BaseCommand):
    help = 'Sets initial structure for database'

    def handle(self, *args, **options):
        year = date.today().year
        if date.today().month > 6:
            year += 1
        run, created = Run.objects.get_or_create(year=year)
        
