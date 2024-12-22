from django.urls import path

from cars.views import car_page_view

urlpatterns = [
    path('cars/', car_page_view)
]
