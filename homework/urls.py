from django.urls import path

from homework.views import home_page_view, about_page_view, interests_page_view, contact_page_view

urlpatterns = [
    path('', home_page_view),
    path('about/', about_page_view),
    path('interests', interests_page_view),
    path('contact/', contact_page_view)
]
