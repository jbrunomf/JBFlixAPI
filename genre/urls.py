from django.urls import path
from genre.views import GenreCreateListView

urlpatterns = [
    path('', GenreCreateListView.as_view(), name='genre_list'),
]
