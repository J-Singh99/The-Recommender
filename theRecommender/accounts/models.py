from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User(AbstractUser):
    #username firstname lastname email password 
    image      = models.ImageField(upload_to='profile_img', default='profile_img/image.jpg' )
    university = models.CharField(max_length=100, null=True, blank=True) # # here means teacher kya hai like software engineer is name is correct for thi
    desciption = models.TextField(null=True, blank=True) 

class Tasks(models.Model):
    task        = models.CharField(max_length=100)
    deadline    = models.DateTimeField()
    completed   = models.BooleanField(default=False)
    user        = models.ForeignKey( User, on_delete=models.CASCADE)


