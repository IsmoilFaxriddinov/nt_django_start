from django.shortcuts import render

def car_page_view(request):
    return render(request, 'cars.html')
