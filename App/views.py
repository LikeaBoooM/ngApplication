from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework import status
from .serializers import CarsCreateSerializer, RatesCreateSerializer, CelcirusSerializer
from .models import Car, Rate, Movie, Celcius
from django.views.generic import ListView
from .CarApiOut import checkModel, checkTitle
from django.db.models import Avg, Count
from . forms import MovieForm


def startview(request):
    return render(request, "ngApplication/base.html")


class CarsNG(APIView):
    def post(self, request):
        if request.data:
            make = request.data['make']
            model = request.data['model']
            check = checkModel(make, model)

            if check == 1:
                serializer = CarsCreateSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response("This model doesn't exist for that make !")
        return Response("No data in request !")

    def get(self, request):
        caravg = Car.objects.annotate(avg_rating=Avg('rate__grade')).values().order_by('id')
        if caravg:
            return Response(caravg, status=status.HTTP_200_OK)
        return Response("No data here.", status=status.HTTP_204_NO_CONTENT)

    def delete(self, request):
        cars = Car.objects.all()
        cars.delete()
        return Response("Objects deleted", status=status.HTTP_200_OK)


class DeleteCar(APIView):
    def get(self, request, id):
        car = get_object_or_404(Car, pk=id)
        serializer = CarsCreateSerializer(car)
        if serializer:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, id, format=None):
        car = get_object_or_404(Car, id=id)
        if car:
            car.delete()
            return Response("Car with id: {} deleted".format(id), status=status.HTTP_200_OK)
        return Response("There is no car with this id", status=status.HTTP_204_NO_CONTENT)


class RateCar(APIView):
    def post(self, request):
        serializer = RatesCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        rates = Rate.objects.all()
        serializer = RatesCreateSerializer(rates, many=True)

        if serializer:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request):
        rates = Rate.objects.all()
        if rates:
            rates.delete()
            return Response("All rates got deleted", status=status.HTTP_204_NO_CONTENT)
        return Response("No rates here", status=status.HTTP_404_NOT_FOUND)


class Popular(APIView):
    def get(self, request):
        number_of_rates = Car.objects.annotate(rates_number=Count('rate')).values().order_by('id')
        if number_of_rates:
            return Response(number_of_rates, status=status.HTTP_200_OK)
        return Response("There is not data", status=status.HTTP_204_NO_CONTENT)


def newMovie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            data = checkTitle(title)
            duration = data[1]
            urltoimg = data[2]
            movie = form.save(commit=False)
            print(duration)
            print(urltoimg)
            movie.duration = duration
            movie.url = urltoimg
            movie.save()
    else:
        form = MovieForm()

    stuff_for_frontend = {
        'form': form,
    }

    return render(request, 'ngApplication/movie_form.html', stuff_for_frontend)


class ListViewMovies(ListView):
    model = Movie
    template_name = 'ngApplication/list_movie.html'


def data(request):
    return render(request, 'index.html')


class home(APIView):
    def get(self, request):
        celcius = Celcius.objects.all()
        serializer = CelcirusSerializer(celcius, many=True)
        if serializer:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)

    def post(self, request):
        if request.data:
            serializer = CelcirusSerializer(request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)
        return Response('No data in here')
