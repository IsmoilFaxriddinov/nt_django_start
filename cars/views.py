from django.shortcuts import render
from cars.models import CarsModel

app_name="cars"

def car_page_view(request):
    cars = CarsModel.objects.all()

    context = {
        "cars": cars
    }

    return render(request, 'cars.html', context)