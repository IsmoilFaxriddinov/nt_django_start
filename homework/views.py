from django.shortcuts import render

# Create your views here.

def home_page_view(request):
    return render(request, 'main.html')

def about_page_view(request):
    return render(request, 'about.html')

def interests_page_view(request):
    return render(request, 'interests.html')

def contact_page_view(request):
    return render(request, 'contact.html')