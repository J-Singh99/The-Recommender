from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('movies', views.movies, name='movies'),
    re_path(r'movies/(?P<id>\d+)/$', views.movie, name='movie'),
    path('movies/search', views.searchmovie, name='searchmovie'),
]