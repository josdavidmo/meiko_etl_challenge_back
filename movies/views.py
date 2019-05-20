from rest_framework import generics

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieList(generics.ListAPIView):
  """
  get:
  Return a list of movies.
  """
  queryset = Movie.objects.all()
  serializer_class = MovieSerializer
