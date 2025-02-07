from django.test import TestCase
from users.models import CustomUser, Rating, History, Cars
from django.contrib.auth.hashers import make_password 


class UserTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            username='testuser12',
            email="testuser@gmail.com",
            uuid=1,
            tuid=2,
            password=make_password('secret'), 
            is_superuser=True,
            is_staff=True,
            is_active=True,
            last_login=None,
            phone=None,
            first_name=None,
            last_name=None,
        )

        car = Cars.objects.create(
            model='carModel',
            number='12ab123',
            color='red',
            user=self.user
        )

    def test_user(self):
        print('\n test_user test....')  
        self.assertEqual(self.user.username, 'testuser12')
        self.assertEqual(self.user.email, 'testuser@gmail.com')
        self.assertEqual(self.user.uuid, 1)
        self.assertEqual(self.user.tuid, 2)
        print('complete!')  

    def test_user_history(self):
        print('\n test_user_history test....')  
        user_history = History.objects.get(user=self.user)
        self.assertEqual(user_history.rides, 0)
        self.assertEqual(user_history.bookings, 0)
        self.assertEqual(user_history.activity, 0)
        self.assertEqual(user_history.saved, 0)
        self.assertEqual(user_history.spend, 0)
        self.assertEqual(user_history.cancelled, 0)
        self.assertEqual(user_history.user, self.user)
        print('complete!')  

    def test_user_rating(self):
        print('\n test_user_rating test....')
        user_rating = Rating.objects.get(user=self.user)
        self.assertEqual(user_rating.rating, 5)
        self.assertEqual(user_rating.user, self.user)
        print('complete!')  

    def test_user_car(self):
        print('\n test_user_car start...')
        car = Cars.objects.get(user=self.user)
        self.assertEqual(car.color, 'red')
        self.assertEqual(car.model, 'carModel')
        self.assertEqual(car.number, '12ab123')
        self.assertEqual(car.user, self.user)
        print('complete!')  

