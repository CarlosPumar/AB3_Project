from tweepy.streaming import Stream
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


class Stream_Twitter(Stream):

    channel_layer = get_channel_layer()

    def on_status(self, status):
        try:
            async_to_sync(self.channel_layer.group_send)(
                "twitter",
                {
                    "type": "player.message",
                    "text": status.text
                },
            )
        except:
            print("No se ha podido conectar")

    def on_error(self, status):
        if status == 420:
            print("error : {}".format(str(status)))

    def on_connect(self):
        print("connected")
        return super().on_connect()
