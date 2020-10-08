from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.chat, name='chat'),
    path('creategrp/', views.create_group, name='creategrp'),
    path('search/', views.search, name='search'),
    re_path(r'personal/(?P<pk>\d+)/$', views.chat_personal, name='personal_chat'),
    re_path(r'grp/(?P<pk>\d+)/$', views.chat_grp, name='grp_chat'),
    re_path(r'deleteuser/(?P<uk>\d+)/(?P<gk>\d+)$', views.removeuser, name='kickoutuser')
]