import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

class NotificationConsumer(WebsocketConsumer):

    def connect(self):
        print('connect')
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'notification_%s' % self.room_name
        print(self.room_group_name)
        print(self.channel_layer)
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        print('disconnect')
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        print('receive')
        # Receive message from WebSocket
        print(text_data)
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': 'product added',
            }
        )

    def notify(self, event):
        print('tasif consumer')
        # Receive message from room group
        text = event['message']
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'text': text
        }))