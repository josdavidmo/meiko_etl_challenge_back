from django.urls import path

from movies import views

urlpatterns = [
    path('movie/', views.MovieList.as_view()),
    path('moviebyactor/', views.MovieByActorList.as_view()),
    path('moviebydirector/', views.MovieByDirectorList.as_view()),
    path('moviebygender/', views.MovieByGenderList.as_view())
]
