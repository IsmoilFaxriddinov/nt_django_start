from django.urls import path
from users.views import home_page_view
urlpatterns = [
    path('/hello', home_page_view())
]
