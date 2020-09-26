from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    club_tag = models.CharField(max_length=3, unique=True,default="DEF")
    uni_tag = models.CharField(max_length=3, unique=True,default="000")

class AdminOf(models.Model):
    event      = models.ForeignKey(events, verbose_name='event', on_delete= models.CASCADE)
    admin       = models.ForeignKey(User, verbose_name='user', on_delete= models.CASCADE)

class RegisteredEvents(models.Model):
    event      = models.ForeignKey(events, verbose_name='event', on_delete= models.CASCADE)
    user      = models.ForeignKey(User, verbose_name='user', on_delete= models.CASCADE)

class events(models.Model):
    #so event id will be given implicitly by django 
    creator = models.ForeignKey(User, on_delete= models.CASCADE)
    eventname = models.CharField(max_length=100, unique=True) 
    description = models.TextField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    venue = models.CharField(max_length=100, unique=True) 
    event_tags = models.ForeignKey(Tag, on_delete= models.CASCADE)

    #jazzy b, you have the posts wala thing, shall add it
    
