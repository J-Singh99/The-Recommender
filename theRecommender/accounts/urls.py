from django.urls import path, re_path
from . import views

urlpatterns = [
    path('chat/$', views.chat, name='chat'),
    path('', views.index, name='index'),

]