from .twitter.stream import Stream_Twitter
from .twitter.data import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET, ID_ACCOUNT

stream = Stream_Twitter(consumer_key=CONSUMER_KEY,
                        consumer_secret=CONSUMER_SECRET,
                        access_token=ACCESS_TOKEN,
                        access_token_secret=ACCESS_TOKEN_SECRET)

stream.filter(follow=[ID_ACCOUNT], threaded=True)
