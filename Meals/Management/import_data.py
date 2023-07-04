import csv
from typing import Any, Optional
from django.core.management.base import BaseCommand
from Meals.models import Food

class Command(BaseCommand):
    help = 'Import dishes from CSV file'

    def handle(self, *args: Any, **options):
        filename = 'restaurants_small.csv'
        with open(filename,'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                dish = Food.objects.create(

                    id = row['id'],
                    name = row['name'],
                    location = row['location'],
                    items = row['items'],
                    lat_long = row['lat_long'],
                    full_details = row['full_details']
                )
        self.stdout.write(self.style.SUCCESS('Data Imported Successfully.'))