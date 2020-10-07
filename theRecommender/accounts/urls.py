from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todo/addtask', views.addTask, name='addtask'),
    re_path(r'todo/deletetask/(?P<id>\d+)/$', views.deleteTask, name='deletetask'),
    path('todo/markcomplete', views.markcomplete, name='markcomplete')
]
