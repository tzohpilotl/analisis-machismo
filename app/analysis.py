from dictionary_tagger import DictionaryTagger
from spaghetti import spaghetti as spgt
from twitter_miner import TwitterMiner
from tweet_formatter import TweetFormatter
from pydoc

if __name__ == '__main__':
"""When the Python interpreter reads a source file, it executes all of the code found in it.
Before executing the code, it will define a few special variables. For example, if the python interpreter is running that module (the source file) as the main program, it sets the special __name__ variable to have a value "__main__". If this file is being imported from another module, __name__ will be set to the module's name."""

    miner = TwitterMiner('keys.ini', 'twitter_data.txt', 1000)
    miner.mine('tracks.csv')

    formatter = TweetFormatter('twitter_data.txt')
    tweets = formatter.convert2json()
    tweets = formatter.convert2text(tweets, 'formatted_tweets.txt')
    tweets = formatter.clean_tweets(tweets)
    tweets = [tweet.split() for tweet in tweets]
#    print(tweets)

    tagger = DictionaryTagger(['./misoginy_dictionary.yml'])
    postagged_sents = spgt.pos_tag_sents(tweets)    
    tagged_sents = tagger.tag(postagged_sents)

    for sent in tagged_sents:
        print(sent)
