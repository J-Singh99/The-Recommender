from django.urls import path,re_path
from . import views

urlpatterns = [
    path('test', views.test, name='test'),
    path('main', views.main, name='main'),
    path('movie', views.movie, name='movie'),
    ]