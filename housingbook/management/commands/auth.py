# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import csv

class Command(BaseCommand):
    help = 'Adding users from csv file'
#settings.configure()
    def handle(self, *args, **options):
        with open('/home/aboreil/Documents/design4green/GreenHB/helper/acces.csv') as csvfile:
            users_info = csv.DictReader(csvfile, delimiter=';')
            for row in users_info:
                p = User.objects.create_user(row['identifiant'], '', row['password'])
                p.save()
print("Users added")
