from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from channels.auth import login
from django.contrib.auth.models import AnonymousUser, User


class WSConsumer(WebsocketConsumer):

    def connect(self):

        user = self.scope['user']

        if user != AnonymousUser():

            async_to_sync(self.channel_layer.group_add)(
                "twitter", self.channel_name)
            self.accept()

        else:
            super().close()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            "twitter", self.channel_name)
        super().disconnect(code)

    def player_message(self, event):
        print("sending...")
        self.send(text_data=event["text"])
