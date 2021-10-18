from tweepy.streaming import Stream
from .logic import manage_message


class Stream_Twitter(Stream):

    # When a tweet is recived, 'manage_message' manage the tweet

    def on_status(self, status):
        manage_message(status.text)

    def on_error(self, status):
        if status == 420:
            print("error : {}".format(str(status)))

    def on_connect(self):
        print("connected - twitter")
        return super().on_connect()
