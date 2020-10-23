from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.song, name='song'),
    path('song2/', views.relatedSongs, name='song2')
]
#<list:id
