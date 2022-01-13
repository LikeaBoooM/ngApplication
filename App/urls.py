from .views import CarsNG, DeleteCar, RateCar, Popular, CarsNG, startview
from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url
from . import views
from . views import ListViewMovies

urlpatterns = [
    path('', startview, name='startview'),
    path('cars/<int:id>/', DeleteCar.as_view(), name='cars-ng-delete'),
    path('rate/', RateCar.as_view(), name='cars-ng-rate-car'),
    path('popular/', Popular.as_view(), name='cars-ng-popular'),
    path('cars/', CarsNG.as_view(), name='cars-ng-avg-rates'),
    path('create/', views.newMovie, name='create'),
    path('show/', ListViewMovies.as_view(), name='list'),
    path('fuzzy/', views.home.as_view(), name='home'),
]