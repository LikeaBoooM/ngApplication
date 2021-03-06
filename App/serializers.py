from .models import Car, Rate, Celcius
from rest_framework import serializers


class CarsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class RatesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ['car_id', 'grade']


class CelcirusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Celcius
        fields = '__all__'
