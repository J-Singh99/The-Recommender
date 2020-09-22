import json
import channels
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Message
from asgiref.sync import sync_to_async
from channels_presence.models import Room
from channels_presence.decorators import remove_presence
from channels_presence.decorators import touch_presence

def uniquepk(pk1, pk2):
    if(pk1 > pk2):
        return pk1 + '_to_' + pk2
    else:
        return pk2 + '_to_' + pk1

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = await channels.auth.get_user(self.scope)
        self.room_name = self.scope['url_route']['kwargs']['pk']
        chat_type = self.scope['url_route']['kwargs']['type']
        if(chat_type == 'grp'):
            self.room_group_name = 'chat_grp_%s' % self.room_name
        elif(chat_type == 'personal'):
            uniquekey = uniquepk(self.room_name, str(self.user.pk))            
            self.room_group_name = 'chat_personal_%s' % uniquekey
        if self.user.is_authenticated:
            # Join room group
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            self.room = await self.create_user(self.room_group_name, self.channel_name, self.user)
            await self.accept()

    @database_sync_to_async
    def create_user(self, group_name, channel_name, user=None):
        return Room.objects.add(group_name, channel_name, self.user)
    
    @database_sync_to_async
    def remove_user(self, group_name, channel_name):
        Room.objects.remove(group_name, channel_name)

    async def disconnect(self, close_code):
        # Leave room group
        await self.remove_user(self.room_group_name, self.channel_name)
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    #@touch_presence
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        message_obj = await self.create_chat_message(self.user, message)
        timestamp = message_obj.timestamp.strftime("%B %d, %Y,  %I:%M %p")
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': self.user.username,
                'timestamp': timestamp
            }
        )

    async def chat_message(self, event):
        message = event['message']
        user = event['user']
        timestamp = event['timestamp']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'user': user,
            'timestamp': timestamp
        }))
        
    @database_sync_to_async
    def create_chat_message(self, user, msg):
        return Message.objects.create(group=self.room_group_name, sender=user, message=msg)