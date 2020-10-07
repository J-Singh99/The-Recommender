from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tasks(models.Model):
    task        = models.CharField(max_length=100)
    deadline    = models.DateTimeField()
    completed   = models.BooleanField(default=False)
    user        = models.ForeignKey( User, on_delete=models.CASCADE)

