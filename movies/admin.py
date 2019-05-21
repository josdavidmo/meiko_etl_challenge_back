from django.contrib import admin
from django.db.models import Sum, Func, F
from django.utils.translation import gettext_lazy as _

from movies.models import Movie


class MoviesFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _("Top Filters")

    # Parameter for the filter that will be used in the URL query.
    parameter_name = "tops"

    def lookups(self, request, model_admin):
        if request.user.is_superuser:
            return (("raised_most_money",
                     _("Which are the 10 movies that raised the most money?")),
                    ("raised_least_money",
                     _("Which are the 10 movies that least the most money?")),
                    ("spent_most_produce_money",
                     _("Which are the 7 films that spent the most money to "
                       "produce?")),
                    ("spent_lest_produce_money",
                     _("What are the 7 films that spent the least money to "
                       "produce?")),
                    ("raised_most_money_year",
                     _(
                         "Which movie genre raised the most money for each year?")),
                    ("top_genre",
                     _("Which genre do people like best?")),
                    ("top_directors",
                     _("Which 5 directors have the best reputation?")),
                    )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        return queryset


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("id",) + Movie.HEADERS
    list_filter = (MoviesFilter,)
    change_list_template = "movies/movies_changelist.html"
    list_per_page = 10

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        if request.GET.get("tops") == "raised_most_money":
            extra_context["list"] = Movie.objects.exclude(
                gross__isnull=True).values_list(
                "movie_title", flat=True).order_by("-gross")[:10]
        if request.GET.get("tops") == "raised_least_money":
            extra_context["list"] = Movie.objects.exclude(
                gross__isnull=True).values_list(
                "movie_title", flat=True).order_by("gross")[:10]
        if request.GET.get("tops") == "spent_most_produce_money":
            extra_context["list"] = Movie.objects.exclude(
                budget__isnull=True).values_list(
                "movie_title", flat=True).order_by("-budget")[:7]
        if request.GET.get("tops") == "spent_lest_produce_money":
            extra_context["list"] = Movie.objects.exclude(
                budget__isnull=True).values_list(
                "movie_title", flat=True).order_by("budget")[:7]
        if request.GET.get("tops") == "raised_most_money_year":
            extra_context["list"] = Movie.objects.annotate(
                genre=Func(F("genres"),
                           function="unnest")).values(
                "genre").values_list("genre", flat=True).annotate(
                total=Sum("gross")).order_by(
                "-total")[:1]
        if request.GET.get("tops") == "top_genre":
            extra_context["list"] = Movie.objects.annotate(
                genre=Func(F("genres"),
                           function="unnest")).values(
                "genre").values_list("genre", flat=True).annotate(
                total=Sum("cast_total_facebook_likes")).order_by(
                "-total")[:1]
        if request.GET.get("tops") == "top_directors":
            extra_context["list"] = Movie.objects.exclude(
                director_name="").values_list("director_name",
                                              flat=True).annotate(total=Sum(
                "director_facebook_likes")).order_by("-total")[:5]
        return super(MovieAdmin, self).changelist_view(request,
                                                       extra_context=extra_context)
