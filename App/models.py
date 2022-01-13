from django.db import models

# Create your models here.


class Car(models.Model):
    make = models.CharField(max_length=180)
    model = models.CharField(max_length=180, unique=True)

    def __str__(self):
        return self.make


class Rate(models.Model):
    class Ratings(models.IntegerChoices):
        One = 1
        Two = 2
        Three = 3
        Four = 4
        Five = 5

    grade = models.IntegerField(choices=Ratings.choices)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)



class Movie(models.Model):
    title = models.CharField(max_length=100)
    duration = models.CharField(max_length=100, null=True)
    url = models.CharField(max_length=200, null=True)


class Celcius(models.Model):
    humidity = models.FloatField(max_length=100)
    temeperature = models.FloatField(max_length=100)
    oventemperature = models.IntegerField()

    def __str__(self):
        return str(self.temeperature)
