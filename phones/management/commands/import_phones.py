import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
        for phone in phones:
            # print(phone)
            phone = Phone(name=phone['name'])
            phone.save()
        

    # print(handle('phones.csv'))     

            # TODO: Добавьте сохранение модели
            # pass
