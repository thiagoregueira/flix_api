import csv
from datetime import datetime
from django.core.management.base import BaseCommand

from actors.models import Actor


class Command(BaseCommand):
    help = 'Import actors from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Path to the CSV file',
        )

    def handle(self, *args, **kwargs):
        file_name = kwargs['file_name']

        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Actor.objects.create(
                    name=row['name'],
                    birthday=datetime.strptime(row['birthday'], '%Y-%m-%d').date(),
                    nationality=row['nationality'],
                )
                self.stdout.write(self.style.NOTICE(f'Actor {row["name"]} imported successfully'))

        self.stdout.write(self.style.SUCCESS('All actors imported successfully'))
