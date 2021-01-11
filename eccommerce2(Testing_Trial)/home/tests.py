from django.test import TestCase, Client
# from dashboard.models import Additem
from django.urls import reverse
#from model_bakery import baker
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eccommerce2.settings")
django.setup()
from django.core.management import call_command

client = Client()


class HomeTest(TestCase):
    # def setUp(self):
    #     self.chair1 = Additem.objects.create(price=10)

    def test_home(self):
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_reg(self):
        response = client.get(reverse('reg'))
        self.assertEqual(response.status_code, 200)

    def test_log(self):
        response = client.get(reverse('log'))
        self.assertEqual(response.status_code, 200)

    # def test_get_all_chairs(self):
    #     response = client.get(reverse('chairs'))
    #     chairs = Additem.objects.filter(category='chairs')
    #     self.assertEqual(response.data, chairs)
    #     self.assertEqual(response.status_code, 200)

    # def test_get_all_armchairs(self):
    #     response = client.get(reverse('armchairs'))
    #     armchairs = Additem.objects.filter(category='armchairs')
    #     self.assertEqual(response.data, armchairs)
    #     self.assertEqual(response.status_code, 200)
    