from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from key_reader import KeyReader

class _StdOutListener(StreamListener):
    """Wrapper for StreamListener. Allows a limited number of tweets retrieved
    and dumping data to a file
    """

    def __init__(self, max_tweets, output_filename=None):
        super(_StdOutListener, self).__init__()
        self.mined_tweets = 0
        self.max_tweets = max_tweets
        try:
            self.output_file = open(output_filename, "w")
        except TypeError as err:
            self.output_file = None

    def on_data(self, data):
        """Check if it already retrieved the established number of tweets and
        handles the dumping of data
        """ 

        if self.output_file is None:
            print(data)
        else:
            self.output_file.write(data)
        self.mined_tweets += 1
        try:
            if self.mined_tweets >= self.max_tweets:
                raise RuntimeError
        except RuntimeError:
            print("Mined {} tweets".format(self.mined_tweets))
            return False
        else:
            return True

    def on_error(self, status):
        print(status)

class TwitterMiner():
    """Exposes the whole chain needed to retrieve data from the Twitter stream
    from reading the keys, create an oAuth object,  
    """

    def __init__(self, keys_file='keys.ini', output_file=None, max_tweets=10):
        self.keys_file = keys_file
        self.output_file = output_file
        self.max_tweets = max_tweets

    def connect(self):
        """Get keys and connect to Twitter through OAuth """
        self.key_reader = KeyReader()
        self.keys = self.key_reader.read('keys.ini', 'keys')

        listener = _StdOutListener(self.max_tweets, self.output_file)
        auth = OAuthHandler(self.keys['consumer_key'], self.keys['consumer_secret'])
        auth.set_access_token(self.keys['access_token'], self.keys['access_token_secret'])
        self.stream = Stream(auth, listener)

    def mine(self, track_words, output_file=None):
        """Retrieve tweets with text that matches track_words. """

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
