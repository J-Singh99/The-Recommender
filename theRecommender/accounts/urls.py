from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todo/', views.todo, name='todo'),
    path('todo/addtask', views.addTask, name='addtask'),
    path('todo/edittask', views.editTask, name='edittask'),
    re_path(r'todo/deletetask/(?P<id>\d+)/$', views.deleteTask, name='deletetask'),
    path('todo/markcomplete', views.markcomplete, name='markcomplete'),
    path('accounts/login/', views.CustomLoginView, name='login'),
    path('accounts/signup/', views.CustomSignUpView, name='signup'),
    path('accounts/logout/', views.signout, name='logout'),
]
