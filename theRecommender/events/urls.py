from django.urls import path,re_path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from . import views

urlpatterns = [
    path('', views.event_feed, name='events'),
    path('addevent/', views.add_event, name='addevent'),
    re_path('deletevent/(?P<id>\d+)/$', views.delete_event, name='deletevent'),
    re_path('registerevent/(?P<id>\d+)/$', views.register_event, name='registerevent'),
    #re_path(r'^(?P<pk>\d+)/showattendance/$', views.showattendance, name='showattendance')
    #(?P<pk>\d+)/$
    re_path('readmore/(?P<id>\d+)/$', views.read_more, name='readmore'),
    #path('', PostListView.as_view(), name='blog-home'),
    #path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    #path('', views.home, name='blog-home'),
]