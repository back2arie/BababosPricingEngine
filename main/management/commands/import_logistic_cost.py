from django.core.management.base import BaseCommand
from main.models import LogisticFleet, LogisticCost
from csv import reader

class Command(BaseCommand):
    help = "Seed data from CSV files"
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')


    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        try:
            with open(file_path, 'r') as csvfile:
                csv_reader = reader(csvfile, delimiter=',')
                next(csv_reader)  # skip header row
                for row in csv_reader:
                    fleet = LogisticFleet.objects.get(type=row[0])
                    LogisticCost.objects.get_or_create(
                        fleet_id=fleet.id,
                        origin=row[1],
                        destination=row[2],
                        cost=row[3],
                    )
                self.stdout.write(self.style.SUCCESS('Data imported successfully'))
        except Exception as e:
            self.stdout.write(self.style.ERROR('Error importing data'))
            print('%s' % type(e))