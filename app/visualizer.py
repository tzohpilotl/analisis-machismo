import sys
import json

if __name__ == '__main__':
    tweets_data_path = './twitter_data.txt'

    tweets_data = []
    with open(tweets_data_path, "r") as tweets_file:
        for line in tweets_file:
            try:
                tweet = json.loads(line)
                tweets_data.append(tweet)
            except:
                continue

    print('Tienes ' + str(len(tweets_data)) + ' tweets')

    for tweet in tweets_data:
        try:
            print(tweet['text'])
        except KeyError:
            print("Skip malformed tweet")
        
    input('Press enter to continue...')
