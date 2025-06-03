from django.core.management.base import BaseCommand
from accounts.models import StudentProfile


class Command(BaseCommand):
    help = 'Insert student data into the database'

    def handle(self, *args, **kwargs):
        # Example data to insert
        pass