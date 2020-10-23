from django.db import models
from accounts.models import User
# Create your models here.


class songInfo(models.Model):
    user_id = models.ForeignKey(User, on_delete= models.CASCADE)
    song = models.CharField(max_length=100, unique=True) 
    listen_count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.song


