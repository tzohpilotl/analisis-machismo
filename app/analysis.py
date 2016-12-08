import pydoc
from dictionary_tagger import DictionaryTagger
from spaghetti import spaghetti as spgt
from twitter_miner import TwitterMiner
from tweet_formatter import TweetFormatter

def main(keys='keys.ini', raw_tweets_file='twitter_data.txt', no_tweets=1000,
         tracked_words_file='tracks.csv',
         formatted_tweets_file='formatted_tweets.txt',
         dictionaries=['misoginy_dictionary.yml', 'curses_dictionary.yml']):
    """When the Python interpreter reads a source file, it executes all of the 
    code found in it. Before executing the code, it will define a few special 
    variables. For example, if the python interpreter is running that module 
    (the source file) as the main program, it sets the special __name__ 
    variable to have a value "__main__". If this file is being imported from 
    another module, __name__ will be set to the module's name.
    """

    miner = TwitterMiner(keys, raw_tweets_file, no_tweets)
    miner.mine(tracked_words_file)

    formatter = TweetFormatter(raw_tweets_file)
    tweets = formatter.convert2json()
    tweets = formatter.convert2text(tweets, formatted_tweets_file)
    tweets = formatter.clean_tweets(tweets)
    tweets = [tweet.split() for tweet in tweets]

    tagger = DictionaryTagger(dictionaries)
    postagged_sents = spgt.pos_tag_sents(tweets)    
    tagged_sents = tagger.tag(postagged_sents)

    for sent in tagged_sents:
        print(sent)

if __name__ == '__main__':
    import plac; plac.call(main)
