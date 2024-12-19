from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_page_view(request):
    return HttpResponse("Hello world")

def home2_page_view(request):
    return HttpResponse("I am a Superman !")

def home3_page_view(request):
    return render(request, 'home.html')