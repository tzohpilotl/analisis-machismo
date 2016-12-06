import sys
import json
import re

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

    tweet_list = []
    for tweet in tweets_data:
        try:
            #Remove hashtags, usernames and links
            #print(tweet['text'])
            tweet_list.append(re.sub(r'((@|#|_|-)[A-Za-z0-9]+)|(RT|retweet|from|via)(?:\b\W*@(\w+))+|(http\S+)','',tweet['text']))
        except KeyError:
            #print("Skip malformed tweet")
            continue
    print(tweet_list)


    #Remove usernames and hashtags
    #print(re.sub(r'(@[A-Za-z0-9]+)|(#[A-Za-z0-9]+)|(_[A-Za-z0-9]+)','',tweet_list))
    #print(re.sub(r'(@[A-Za-z0-9]+)','',tweet_list))

    #input('Press enter to continue...')
