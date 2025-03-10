from django.urls import path
from genre.views import GenreCreateListView, GenreRetrieveUpdateDestroyView

urlpatterns = [
    path('', GenreCreateListView.as_view(), name='genre_list'),
    path('/<int:pk>', GenreRetrieveUpdateDestroyView.as_view(), name='genre_detail_view'),
]
