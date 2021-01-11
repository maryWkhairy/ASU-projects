from django.contrib.auth.models import User
from django.test import TestCase


# Create your tests here.

# class RegistrationTestCase(TestCase):
#     def setUp(self):
#         User.objects.create_user(username="marc", email="marc", password="marc", password_confirm="marc")
#         User.objects.create_user(username="michael", email="michael", password="marc", password_confirm="michael")
#
#     def test_password_confirm_fail(self):
#         user = User.objects.get(id=2)
#         self.assertFalse(user.password, user.password_confirm)
