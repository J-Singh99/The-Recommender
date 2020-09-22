from django.urls import path, re_path
from . import views

urlpatterns = [
    path('chat/', views.chat, name='chat'),
    path('chat/creategrp/', views.create_group, name='creategrp'),
    path('chat/search/', views.search, name='search'),
    re_path(r'chat/personal/(?P<pk>\d+)/$', views.chat_personal, name='personal_chat'),
    re_path(r'chat/grp/(?P<pk>\d+)/$', views.chat_grp, name='grp_chat')
]