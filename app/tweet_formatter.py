import sys
import re
import json

class TweetFormatter():

    def __init__(self, source_file='twitter_data.txt'):
        self.tweets_source = source_file

    def convert2json(self, tweets_source=None):
        tweets_data = []
        if tweets_source is None:
            if self.tweets_source is not None:
                tweets_source = self.tweets_source
            else:
                raise ValueError("You need to specify a file")

        with open(tweets_source, "r") as tweets_file:
            for line in tweets_file:
                try:
                    tweet = json.loads(line)
                    tweets_data.append(tweet)
                except:
                    continue
        return tweets_data

    def convert2text(self, tweets_data=None, output_file=None):
        tweets_text = []
        if tweets_data is None:
            raise ValueError("Provide convert2json's output as parameter")
        for tweet in tweets_data:
            try:
                tweets_text.append(tweet['text'])
            except KeyError:
                continue
        if output_file is not None:
            with open(output_file, "w") as output:
                for tweet in tweets_text:
                    output.write(tweet + '\n')
        return tweets_text

    def clean_tweets(self, tweets_text=None):
        tweets_clean = []
        if tweets_text is None:
            raise ValueError("Provide convert2text's output as parameter")
        for tweet in tweets_text:
            try:
                tweets_clean.append(re.sub(r'((@\S+|#\S+)[A-Za-z0-9]+)|(RT|retweet|from|via)(?:\b\W*@(\w+))+|(http\S+)', '', tweet))
            except KeyError:
                continue
        return tweets_clean

    def print_tweets(self, tweets_data=None):
        if tweets_data is None:
            print("Provide convert2json's output as parameter.")
        else:
            for tweet in self.tweets_data:
                try:
                    print(tweet['text'])
                except KeyError:
                    print("Skip malformed tweet")
            input('Press enter to continue...')
