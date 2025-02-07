from django.test import TestCase
from .models import Cities

class CitiesTest(TestCase):

    def setUp(self):
        Cities.objects.bulk_create([
        Cities(name="city1", usage=0),
        Cities(name="city2", usage=0)
    ])

    def test_cities(self):
        print('\n cities test....')  

        city1 = Cities.objects.get(name="city1")
        city2 = Cities.objects.get(name="city2")
        
        self.assertEqual(city1.name, "city1")
        self.assertEqual(city1.usage, 0)
        self.assertEqual(city2.name, "city2")
        self.assertEqual(city2.usage, 0)
        print('complete!')  

