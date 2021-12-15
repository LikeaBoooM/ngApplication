from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework import status
from .serializers import CarsCreateSerializer, RatesCreateSerializer
from .models import Car, Rate
from .CarApiOut import checkModel
from django.db.models import Avg, Count


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
            return Response("This model doesn't exist for that make ! ")
        return Response("No data in request !")

    def get(self, request):
        caravg = Car.objects.annotate(avg_rating=Avg('rate__grade')).values().order_by('id')
        if caravg:
            return Response(caravg, status=status.HTTP_200_OK)
        return Response("No data here.", status=status.HTTP_204_NO_CONTENT)

    def delete(self, request):
        cars = Car.objects.all()
        cars.delete()


class DeleteCar(APIView):
    def delete(self, request, id):
        if id:
            car = get_object_or_404(Car, pk=id)
            car.delete()
            return Response("Car with id: {} deleted".format(id), status=status.HTTP_200_OK)
        return Response("There is no car with this id", status=status.HTTP_400_BAD_REQUEST)


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
        rates.delete()


class Popular(APIView):
    def get(self, request):
        number_of_rates = Car.objects.annotate(rates_number=Count('rate')).values().order_by('id')
        return Response(number_of_rates, status=status.HTTP_200_OK)

