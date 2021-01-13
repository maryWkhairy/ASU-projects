from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eccommerce2.settings")
django.setup()
from dashboard.models import Additem
from django.core.management import call_command


class HomeTest(TestCase, SimpleTestCase):
    def setUp(self):
        self.client = Client()

    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_reg(self):
        response = self.client.get(reverse('reg'))
        self.assertEqual(response.status_code, 200)

    def test_log(self):
        response = self.client.get(reverse('log'))
        self.assertEqual(response.status_code, 200)

    def test_chairs(self):
        response = self.client.get(reverse('chairs'))
        self.assertEqual(response.status_code, 200)

    def test_armchairs(self):
        response = self.client.get(reverse('armchairs'))
        self.assertEqual(response.status_code, 200)

    def test_sofas(self):
        response = self.client.get(reverse('sofas'))
        self.assertEqual(response.status_code, 200)

    def test_beds(self):
        response = self.client.get(reverse('beds'))
        self.assertEqual(response.status_code, 200)

    def test_chaiselognues(self):
        response = self.client.get(reverse('chaiselongues'))
        self.assertEqual(response.status_code, 200)

    def test_shelving(self):
        response = self.client.get(reverse('shelving_units'))
        self.assertEqual(response.status_code, 200)

    def test_tables(self):
        response = self.client.get(reverse('tables'))
        self.assertEqual(response.status_code, 200)

    def test_wardrobes(self):
        response = self.client.get(reverse('wardrobes'))
        self.assertEqual(response.status_code, 200)

    # def test_buyer(self):
    #     response = self.client.get(reverse('buyer'))
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_seller(self):
    #     response = self.client.get(reverse('seller'))
    #     self.assertEqual(response.status_code, 200)
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

