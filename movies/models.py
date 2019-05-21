from django.contrib.postgres.fields import ArrayField
from django.db import models


class Movie(models.Model):
    """
    Represents a movie.
    """
    HEADERS = ("color", "director_name", "num_critic_for_reviews", "duration",
               "director_facebook_likes", "actor_3_facebook_likes",
               "actor_2_name", "actor_1_facebook_likes", "gross", "genres",
               "actor_1_name", "movie_title", "num_voted_users",
               "cast_total_facebook_likes", "actor_3_name",
               "facenumber_in_poster", "plot_keywords", "movie_imdb_link",
               "num_user_for_reviews", "language", "country", "content_rating",
               "budget", "title_year", "actor_2_facebook_likes", "imdb_score",
               "aspect_ratio", "movie_facebook_likes")

    movie_title = models.CharField(max_length=100)
    color = models.CharField(max_length=20)
    director_name = models.CharField(max_length=50)
    actor_1_name = models.CharField(max_length=50)
    actor_2_name = models.CharField(max_length=50)
    actor_3_name = models.CharField(max_length=50)
    director_facebook_likes = models.PositiveIntegerField(null=True)
    actor_3_facebook_likes = models.PositiveIntegerField(null=True)
    actor_2_facebook_likes = models.PositiveIntegerField(null=True)
    actor_1_facebook_likes = models.PositiveIntegerField(null=True)
    num_critic_for_reviews = models.PositiveIntegerField(null=True)
    duration = models.IntegerField(null=True)
    gross = models.BigIntegerField(null=True)
    genres = ArrayField(models.CharField(max_length=20))
    num_voted_users = models.PositiveIntegerField()
    cast_total_facebook_likes = models.PositiveIntegerField()
    facenumber_in_poster = models.PositiveIntegerField(null=True)
    plot_keywords = ArrayField(models.CharField(max_length=20), null=True)
    movie_imdb_link = models.URLField()
    language = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    content_rating = models.CharField(max_length=20)
    budget = models.BigIntegerField(null=True)
    title_year = models.PositiveIntegerField(null=True)
    imdb_score = models.DecimalField(null=True, decimal_places=2, max_digits=3)
    aspect_ratio = models.DecimalField(null=True, decimal_places=2,
                                       max_digits=4)
    movie_facebook_likes = models.PositiveIntegerField()
    num_user_for_reviews = models.PositiveIntegerField(null=True)


class MoviesByActor(object):
    ATTRIBUTES = ['actor_1_name', 'movie_titles', 'total']

    def __init__(self, **kwargs):
        for field in self.ATTRIBUTES:
            setattr(self, field, kwargs.get(field, None))


class MoviesByDirector(object):
    ATTRIBUTES = ['director_name', 'movie_titles', 'total']

    def __init__(self, **kwargs):
        for field in self.ATTRIBUTES:
            setattr(self, field, kwargs.get(field, None))


class MoviesByGender(object):
    ATTRIBUTES = ['genre', 'movie_titles', 'total']

    def __init__(self, **kwargs):
        for field in self.ATTRIBUTES:
            setattr(self, field, kwargs.get(field, None))
