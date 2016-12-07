from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from key_reader import KeyReader

class _StdOutListener(StreamListener):

    def __init__(self, output_filename=None):
        super(_StdOutListener, self).__init__()
        try:
            self.output_file = open(output_filename, "w")
        except TypeError as err:
            self.output_file = None

    def on_data(self, data):
        if self.output_file is None:
            print(data)
        else:
            self.output_file.write(data)
        return True

    def on_error(self, status):
        print(status)

class TwitterMiner():

    def __init__(self, keys_file='keys.ini', output_file=None):
        self.keys_file = keys_file
        self.output_file = output_file

    def connect(self):
        self.key_reader = KeyReader()
        self.keys = self.key_reader.read('keys.ini', 'keys')

        listener = _StdOutListener(self.output_file)
        auth = OAuthHandler(self.keys['consumer_key'], self.keys['consumer_secret'])
        auth.set_access_token(self.keys['access_token'], self.keys['access_token_secret'])
        self.stream = Stream(auth, listener)

    def mine(self, track_words, output_file=None):
        """ This line filter Twitter Streams to capture data by keywords """

        if output_file is not None:
            self.output_file = output_file
        self.connect()
        
        with open(track_words, "r") as t:
            tracks = []
            for line in t:
                tracks.append(line)
            try:
                print("Press Ctrl+C to stop mining tweets...")
                self.stream.filter(languages=["es"], track=tracks)
            except KeyboardInterrupt:
                print("Bye!")
