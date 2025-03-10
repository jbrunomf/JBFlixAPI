from rest_framework import generics

from genre.models import Genre
from genre.serializers import GenreSerializer


class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
