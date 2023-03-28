from channels.generic.websocket import AsyncWebsocketConsumer
import json
import re

class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Retrieve the room name from the URL route's keyword arguments & replacing space with '_' and lowering the case
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_name = re.sub('[^0-9a-zA-Z_]+', '_', self.room_name)

        # Construct the room group name
        self.room_group_name = f'chat_{self.room_name}'

        # Retrieve the user object from the scope
        self.user = self.scope["user"]

        # Add the user's channel name to the room's channel layer group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        # Accept the WebSocket connection
        await self.accept()

        # Send a connected message to the room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'connected_message',
                'message': f'<span class="text-green-500">{self.user.first_name}</span> Joined The Chat !!!',
            }
        )

    async def receive(self, text_data=None, bytes_data=None):
        # Parse the incoming JSON data
        data = json.loads(text_data)
        # Get the message from the data
        message = data['message']
        # Get the first name of the user from the data
        first_name = data['first_name']

        # Send the message to the group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chatroom_message',
                'message':message,
                'first_name':first_name
            }
        )

    async def disconnect(self, close_code):
        # Send a disconnected message to the room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'disconnected_message',
                'message': f'<span class="text-red-500">{self.user.first_name}</span> Left The Chat !!!',
            }
        )

        # Leave the room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def connected_message(self, event):
        # Retrieve the message and type from the event
        type = event['type']
        message = event['message']

        # Send the message to the client/WebSocket
        await self.send(text_data=json.dumps({
            'type':type,
            'message':message
        }))

    async def chatroom_message(self, event):
        # Retrieve the message and sender's first name from the event
        message = event['message']
        first_name = event['first_name']

        # Send the message to the client/WebSocket
        await self.send(text_data=json.dumps({
            'message' : message,
            'first_name' : first_name
        }))

    async def disconnected_message(self, event):
        # Retrieve the message from the event
        type = event['type']
        message = event['message']

        # Send the message to the client/WebSocket
        await self.send(text_data=json.dumps({
            'type':type,
            'message':message
        }))
