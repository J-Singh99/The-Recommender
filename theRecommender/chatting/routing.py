from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^ws/chatting/(?P<type>\w+)/(?P<pk>\d+)/$', consumers.ChatConsumer),
]