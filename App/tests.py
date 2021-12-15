import json
from django.urls import reverse, resolve
from django.test import SimpleTestCase
from .views import RateCar
from rest_framework import status
from .models import Car
from django.test import TestCase, Client
from .serializers import CarsCreateSerializer
from django.db.models import Avg

# Create your tests here.

client = Client()


class ApiUrlsTests(SimpleTestCase):

    def test_rate_is_resolved(self):
        url = reverse('cars-ng-rate-car')
        self.assertEquals(resolve(url).func.view_class, RateCar)


class GetAllCarTest(TestCase):

    def setUp(self):
        Car.objects.create(make='Volkswagen', model='Tiguan')
        Car.objects.create(make='Volkswagen', model='Passat')
        Car.objects.create(make='Audi', model='A4')

    def test_get_all(self):
        self.caravg = Car.objects.annotate(avg_rating=Avg('rate__grade')).values().order_by('id')
        response = client.get(reverse('cars-ng-avg-rates'))
        serializer = CarsCreateSerializer(self.caravg, many=True)
        #self.assertEquals(response.data, serializer.data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)


class CreateOneCarTest(TestCase):

    def setUp(self):
        self.valid_data = {
            'make': 'Volkswagen',
            'model': 'Tiguan'
        }

        self.invalid_data = {
            'make': '',
            'model': 'Tiguan'
        }

    def test_create_valid_car(self):
        response = client.post(
            reverse('cars-ng-avg-rates'),
            data=json.dumps(self.valid_data),
            content_type='application/json'
        )
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)


class CreateRateCar(TestCase):

    def setUp(self):
        self.car1 = Car.objects.create(make="Volkswagen", model="Tiguan")
        self.valid_data = {
            'car_id': self.car1.id,
            'grade': 5,
        }

    def test_create_rate(self):
        response = client.post(
            reverse('cars-ng-rate-car'),
            data=json.dumps(self.valid_data),
            content_type='application/json'
        )
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)


class DeleteCar(TestCase):

    def setUp(self):
        self.car1 = Car.objects.create(make="Volkswagen", model="Tiguan")

    def test_valid_data_delete(self):
        response = client.delete(
            reverse('cars-ng-delete', kwargs={'id': self.car1.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
