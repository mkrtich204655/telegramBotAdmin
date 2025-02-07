from django.test.runner import DiscoverRunner
import unittest
from users.tests import UserTest
from cities.tests import CitiesTest

class TestRunner(DiscoverRunner):

    def build_suite(self, *args, **kwargs):
        test_suite = unittest.TestSuite()
        test_suite.addTest(UserTest('test_user'))
        test_suite.addTest(UserTest('test_user_history'))
        test_suite.addTest(UserTest('test_user_rating'))
        test_suite.addTest(UserTest('test_user_car'))
        test_suite.addTest(CitiesTest('test_cities'))
        return test_suite