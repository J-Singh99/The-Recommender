from django.contrib import admin
from .models import Message, Group, JoinedGroups, JoinedUser
from channels_presence.models import Room, Presence
# Register your models here.
admin.site.register(Message)
admin.site.register(Group)
admin.site.register(JoinedGroups)
admin.site.register(JoinedUser)
admin.site.register(Room)
admin.site.register(Presence)