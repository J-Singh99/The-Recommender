from django.db import models
#from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from accounts.models import User

#need to make a model for tags and user relation
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class club(models.Model):
    tag = models.CharField(max_length=3, unique=True,default="DEF")
    #uni = models.ForeignKey(User.university, verbose_name='university', on_delete= models.CASCADE)
    def __str__(self):
        return self.tag

class events(models.Model):
    creator = models.ForeignKey(User, on_delete= models.CASCADE)
    eventname = models.CharField(max_length=100, unique=True) 
    description = models.TextField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    venue = models.CharField(max_length=100) 
    event_tags = models.ForeignKey(club, on_delete= models.CASCADE)
    #club_tag = models.ForeignKey(club, on_delete= models.CASCADE)
    #uni = models.ForeignKey(User, verbose_name='university', on_delete= models.CASCADE)
    def __str__(self):
        return self.eventname
    
class AdminOf(models.Model):
    event      = models.ForeignKey(events, verbose_name='event', on_delete= models.CASCADE)
    admin       = models.ForeignKey(User, verbose_name='user', on_delete= models.CASCADE)

class RegisteredEvents(models.Model):
    event      = models.ForeignKey(events, verbose_name='event', on_delete= models.CASCADE)
    user      = models.ForeignKey(User, verbose_name='user', on_delete= models.CASCADE)
    
    def __str__(self):
        return self.event.eventname
    


    
