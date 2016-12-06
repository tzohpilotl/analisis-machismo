from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from readkeys import readKeys

class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    keys = readKeys()

    # This handles Twitter authetification and the connection to Twitter Streaming API
    listener = StdOutListener()
    auth = OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
    auth.set_access_token(keys['access_token'], keys['access_token_secret'])
    stream = Stream(auth, listener)

    # This line filter Twitter Streams to capture data by keywords
    with open("csv_file.csv", "r") as t:
        tracks = t.read()
    stream.filter(languages=["es"], track=tracks)
