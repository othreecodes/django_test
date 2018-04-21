import os
from test_plus.test import TestCase
from unittest.mock import patch
from django.conf import settings


class TestUser(TestCase):

    def setUp(self):
        self.user = self.make_user()
        apps_dir = settings.APPS_DIR
        self.FILE = os.path.join(
            str(apps_dir), 'users', 'tests', 'test_mini.py')

    def test__str__(self):
        self.assertEqual(
            self.user.__str__(),
            'testuser'  # This is the default username for self.make_user()
        )

    def test_get_absolute_url(self):
        self.assertEqual(
            self.user.get_absolute_url(),
            '/users/testuser/'
        )

    def test_if_test_mini_file_exists(self):

        self.assertTrue(os.path.exists(
            self.FILE), "You would need to create a test_mini.py file in this directory")

    def get_results_in_file(self):
        results = []
        with open(self.FILE) as fff:
            results = [x.strip() for x in fff]
        return results

    def test_there_is_a_function_called_fizzbuzz_val_in_test_mini_file(self):
        self.assertIn('def fizzbuzz_val(val):', self.get_results_in_file(),
                      "There must be a function named fizzbuzz_val which takes a param val in test_mini.py")

    def test_multiples_of_3_and_5_exists_in_file(self):
        results = self.get_results_in_file()
        self.assertIn('def test_multiples_of_3_and_5(self):', results,
                      "There is a test method called test_multiples_of_3_and_5")
        self.assertIn("self.assertEqual(fizzbuzz_val(15), 'FizzBuzz')", results,
                      "The test method asserts that fizzbuzz_val(15) return 'FizzBuzz'")

    def test_multiples_of_5_alone_exists_in_file(self):
        results = self.get_results_in_file()
        self.assertIn('def test_multiples_of_5_alone(self):', results,
                      'There is a test method called def test_multiples_of_5_alone')
        self.assertIn("self.assertTrue(fizzbuzz_val(5) is 'Buzz')", results,
                      "The tests assert that fizzbuzz_val(5) which equates to 'Buzz' is True")
        self.assertIn("self.assertTrue(fizzbuzz_val(10) is 'Buzz')", results,
                      "The tests assert that fizzbuzz_val(10) which equates to 'Buzz' is True")
        self.assertIn("self.assertTrue(fizzbuzz_val(20) is 'Buzz')", results,
                      "The tests assert that fizzbuzz_val(20) which equates to 'Buzz' is True")
        self.assertIn("self.assertFalse(fizzbuzz_val(8) is 'Buzz')", results,
                      "The tests assert that fizzbuzz_val(8) which equates to 'Buzz' is False")

    def test_multiples_of_3_alone_exists_in_file(self):
        results = self.get_results_in_file()
        self.assertIn('def test_multiples_of_3_alone(self):', results,
                      'There is a test method called def test_multiples_of_3_alone')
        self.assertIn("self.assertTrue(fizzbuzz_val(3) is 'Fizz')", results,
                      "The tests assert that fizzbuzz_val(3) which equates to 'Fizz' is True")
        self.assertIn("self.assertTrue(fizzbuzz_val(99) is 'Fizz')", results,
                      "The tests assert that fizzbuzz_val(99) which equates to 'Fizz' is True")
        self.assertIn("self.assertFalse(fizzbuzz_val(15) is 'Fizz')", results,
                      "The tests assert that fizzbuzz_val(15) which equates to 'Fizz' is False")
        self.assertIn("self.assertFalse(fizzbuzz_val(8) is 'Fizz')", results,
                      "The tests assert that fizzbuzz_val(8) which equates to 'Fizz' is False")