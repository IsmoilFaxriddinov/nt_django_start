from django.urls import path
from cats.views import cat_page_view, cats_page_view
urlpatterns = [
    path('white/', cat_page_view),
    path('black/', cats_page_view)
]
