from django.core.management.base import BaseCommand
from main.models import Product
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
                    if Product.objects.filter(id=row[3]).exists():
                        pass
                    else:
                        Product.objects.create(
                            id=row[3],
                            code=row[2],
                            name=row[4],
                            unit_of_measure=row[6],
                        )
                self.stdout.write(self.style.SUCCESS('Data imported successfully'))
        except Exception as e:
            self.stdout.write(self.style.ERROR('Error importing data'))
            print('%s' % type(e))