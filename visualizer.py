import sys
import json
#import pandas as pd
#import matplotlib.pyplot as plt

if __name__ == '__main__':
    tweets_data_path = './twitter_data.txt'

    tweets_data = []
    tweets_file = open(tweets_data_path, "r")
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue

    print(len(tweets_data))

    print(tweet['text'])
    input('Press enter to continue...')
