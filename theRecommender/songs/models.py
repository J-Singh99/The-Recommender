from django.db import models
from accounts.models import User
# Create your models here.

<<<<<<< HEAD
class songInfo(models.Model):
    user_id = models.ForeignKey(User, on_delete= models.CASCADE)
    song = models.CharField(max_length=100, unique=True) 
    listen_count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.song

=======

class songInfo(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.CharField(max_length=100, unique=True)
    listen_count = models.IntegerField(default=0)

    def __str__(self):
        return self.song
>>>>>>> 581e8d9830035f6b700b5a28c6d976e3e2916698
