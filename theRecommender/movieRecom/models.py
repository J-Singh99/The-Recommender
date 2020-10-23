from django.db import models
from accounts.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class links(models.Model):
    movieid  =   models.IntegerField(primary_key=True)
    imbdid   =   models.IntegerField()
    tmdbid   =   models.IntegerField()

class Ratings(models.Model):
    user     =   models.ForeignKey(User, verbose_name='user', on_delete= models.CASCADE)
    movieid  =   models.ImageField()
    ratings  =   models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5.0)], default=None)