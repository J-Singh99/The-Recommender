from django.contrib import admin
from .models import Post,club,events,AdminOf,RegisteredEvents
# Register your models here.

admin.site.register(Post)
admin.site.register(club)
admin.site.register(events)
admin.site.register(AdminOf)
admin.site.register(RegisteredEvents)
