from django.db import models
from accounts.models import User
# Create your models here.
class Message(models.Model):
    group       = models.CharField(max_length=100)
    sender      = models.ForeignKey(User, verbose_name='sender', on_delete= models.CASCADE)
    message     = models.TextField(null=False)
    timestamp   = models.DateTimeField(auto_now_add=True)


class Group(models.Model):
    group_name  = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image       = models.ImageField(upload_to='profile_img', default='profile_img/image.jpg' )
    admin       = models.ForeignKey(User, verbose_name='admin', on_delete= models.CASCADE)

class JoinedGroups(models.Model):
    group      = models.ForeignKey(Group, verbose_name='group', on_delete= models.CASCADE)
    user       = models.ForeignKey(User, verbose_name='user', on_delete= models.CASCADE)

class JoinedUser(models.Model):
    sender      = models.ForeignKey(User, related_name='%(class)s_sender', verbose_name='sender', on_delete= models.CASCADE)
    receiver    = models.ForeignKey(User, verbose_name='reciever', on_delete= models.CASCADE)