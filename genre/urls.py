from django.urls import path
from genre.views import genre_list_view

urlpatterns = [
    path('', genre_list_view, name='genre_list'),
]
