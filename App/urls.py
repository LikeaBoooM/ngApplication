from .views import CarsNG, DeleteCar, RateCar, Popular, CarsNG
from django.urls import path


urlpatterns = [
    path('cars/<int:id>/', DeleteCar.as_view(), name='cars-ng-delete'),
    path('rates/', RateCar.as_view(), name='cars-ng-rate-car'),
    path('popular/', Popular.as_view(), name='cars-ng-popular'),
    path('cars/', CarsNG.as_view(), name='cars-ng-avg-rates'),
]