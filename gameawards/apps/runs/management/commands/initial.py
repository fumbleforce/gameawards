from django.core.management.base import BaseCommand, CommandError
from datetime import date
from runs.models import Run
from content.models import General

class Command(BaseCommand):
    help = 'Sets initial structure for database'

    def handle(self, *args, **options):
        year = date.today().year
        
        #Current Run
        if date.today().month > 6:
            year += 1
        run, created = Run.objects.get_or_create(year=year, current_run=True)
        
        
        # Info page
        faq , created = General.objects.get_or_create(title='faq', text="empty")
        categories , created = General.objects.get_or_create(title='categories', text="empty")
        rules , created = General.objects.get_or_create(title='rules', text="empty")
        organizers , created = General.objects.get_or_create(title='organizers', text="empty")
        guides , created = General.objects.get_or_create(title='guides', text="empty")
        
        
        
