from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from readkeys import readKeys

class StdOutListener(StreamListener):

    def __init__(self):
        super(StdOutListener, self).__init__()

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':

    key_reader = KeyReader()
    keys = key_reader.read('keys.ini', 'keys')

    # This handles Twitter authetification and the connection to
    # Twitter Streaming API
    listener = StdOutListener()
    auth = OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
    auth.set_access_token(keys['access_token'], keys['access_token_secret'])
    stream = Stream(auth, listener)

    # This line filter Twitter Streams to capture data by keywords
    with open("tracks.csv", "r") as t:
        tracks = []
        for line in t:
            tracks.append(line)
    try:
        stream.filter(languages=["es"], track=tracks)
    except KeyboardInterrupt:
        print("\nKeyboard Interrupted")
        input("press enter to continue.....")
