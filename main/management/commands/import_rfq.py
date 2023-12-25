from django.core.management.base import BaseCommand
from main.models import RequestForQuotation
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
                    RequestForQuotation.objects.get_or_create(
                        customer_id=row[0],
                        product_id=row[1],
                        qty=row[2],
                    )
                self.stdout.write(self.style.SUCCESS('Data imported successfully'))
        except Exception as e:
            self.stdout.write(self.style.ERROR('Error importing data'))
            print('%s' % type(e))