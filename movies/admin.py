from django.contrib import admin
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _

from movies.models import Movie


class MoviesFilter(admin.SimpleListFilter):
  # Human-readable title which will be displayed in the
  # right admin sidebar just above the filter options.
  title = _('Top Filters')

  # Parameter for the filter that will be used in the URL query.
  parameter_name = 'tops'

  def lookups(self, request, model_admin):
    if request.user.is_superuser:
      return (('raised_most_money',
               _('Which are the 10 movies that raised the most money?')),
              ('raised_least_money',
               _('Which are the 10 movies that least the most money?')),
              ('spent_most_produce_money',
               _('Which are the 7 films that spent the most money to '
                 'produce?')),
              ('spent_lest_produce_money',
               _('What are the 7 films that spent the least money to '
                 'produce?')),
              ('raised_most_money_year',
               _('Which movie genre raised the most money for each year?')),
              ('top_genre',
               _('Which genre do people like best?')),
              ('top_directors',
               _('Which 5 directors have the best reputation?')),
              )

  def queryset(self, request, queryset):
    """
    Returns the filtered queryset based on the value
    provided in the query string and retrievable via
    `self.value()`.
    """
    if self.value() == 'raised_most_money':
      return queryset.order_by('-gross')
    elif self.value() == 'raised_least_money':
      return queryset.order_by('gross')
    elif self.value() == 'spent_most_produce_money':
      return queryset.order_by('-budget')
    elif self.value() == 'spent_lest_produce_money':
      return queryset.order_by('budget')
    elif self.value() == 'top_directors':
      qs = Movie.objects.exclude(director_name__isnull=True).values_list(
        'director_name').annotate(likes=Sum(
        'director_facebook_likes')).order_by('-likes')[:5]
      directors = [result[0] for result in list(qs)]
      return queryset


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
  list_display = ('id',) + Movie.HEADERS
  list_filter = (MoviesFilter, 'genres')

  # def get_queryset(self, request):
  #   return Movie.objects.all()
