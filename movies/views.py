from django.db.models import Count, F, Func
from rest_framework import generics

from movies.models import Movie, MoviesByActor, MoviesByDirector, MoviesByGender
from movies.serializers import MovieSerializer, MovieByActorSerializer, \
    MovieByDirectorSerializer, MovieByGenderSerializer
from utils.django.db.models import GroupConcat


class MovieList(generics.ListAPIView):
    """
    get:
    Return a list of movies.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filterset_fields = {"actor_1_name": ["contains"],
                        "actor_2_name": ["contains"],
                        "actor_3_name": ["contains"]}


class MovieByActorList(generics.ListAPIView):
    """
    get:
    Return a list of movies grouped by actor.
    """
    serializer_class = MovieByActorSerializer

    def get_queryset(self):
        qs = Movie.objects.exclude(actor_1_name="").values(
            "actor_1_name").annotate(total=Count("movie_title"),
                                     movie_titles=GroupConcat("movie_title"))
        return [MoviesByActor(**moviebyactor) for moviebyactor in qs]


class MovieByDirectorList(generics.ListAPIView):
    """
    get:
    Return a list of movies grouped by director, order by title_year.
    """
    serializer_class = MovieByDirectorSerializer

    def get_queryset(self):
        qs = Movie.objects.exclude(
            director_name="").values("director_name").annotate(
            total=Count("movie_title"), movie_titles=GroupConcat(
                "movie_title", order_by="title_year DESC"))
        return [MoviesByDirector(**moviebydirector) for moviebydirector in qs]


class MovieByGenderList(generics.ListAPIView):
    """
    get:
    Return a list of movies grouped by gender order by collection.
    """
    serializer_class = MovieByGenderSerializer

    def get_queryset(self):
        qs = Movie.objects.annotate(genre=Func(F('genres'),
                                               function='unnest')).values(
            "genre").annotate(total=Count("movie_title"),
                              movie_titles=GroupConcat(
                                  "movie_title")).order_by('-total')
        return [MoviesByGender(**moviebygender) for moviebygender in qs]
