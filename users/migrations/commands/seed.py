from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import CustomUser
from django.contrib.auth.hashers import make_password 

class Command(BaseCommand):
    help = 'Seed database with test data'

    def handle(self, *args, **kwargs):
        seeder = Seed.seeder()

        seeder.add_entity(CustomUser, 1, {
            'username':  'superuser3',
            'email': "superuser@gmail.com",
            'uuid': 111111,
            'tuid': 11111111,
            'password': lambda x: make_password('secret'), 
            'is_superuser': lambda x: True,
            'is_staff': lambda x: True,
            'is_active': lambda x: True,
            'last_login': None,
            'phone': None,
            'first_name': None,
            'last_name': None,
        })

        seeder.execute()
        self.stdout.write(self.style.SUCCESS('Successfully seeded test data'))
