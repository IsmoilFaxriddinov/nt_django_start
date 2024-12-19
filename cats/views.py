from django.shortcuts import render

# Create your views here.

def cat_page_view(request):
    return render(request, 'cat.html')

def cats_page_view(request):
    return render(request, 'cats.html')