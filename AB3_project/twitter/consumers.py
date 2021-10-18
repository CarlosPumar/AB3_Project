from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class WSConsumer(WebsocketConsumer):

    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            "twitter", self.channel_name)
        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            "twitter", self.channel_name)
        super().disconnect(code)

    def player_message(self, event):
        self.send(text_data=event["text"])
