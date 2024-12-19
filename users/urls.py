from django.urls import path, include
from users.views import home_page_view, home2_page_view, home3_page_view
urlpatterns = [
    path('hello/', home_page_view),
    path("me/", home2_page_view),
    path('helo/', home3_page_view)
]
