from django.core.management.base import BaseCommand
from django_seed import Seed
from cities.models import Cities

class Command(BaseCommand):
    help = 'Seed database with test data'

    def handle(self, *args, **kwargs):
        seeder = Seed.seeder()

        seeder.add_entity(Cities, 10, {
            'name':  lambda x: seeder.faker.text(max_nb_chars=10),
            'usage': lambda x: seeder.faker.random_int(min=0, max=10)
        })

        seeder.execute()
        self.stdout.write(self.style.SUCCESS('Successfully seeded test data'))

