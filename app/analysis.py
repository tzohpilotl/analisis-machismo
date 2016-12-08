import pydoc
import plac
from dictionary_tagger import DictionaryTagger
from spaghetti import spaghetti as spgt
from twitter_miner import TwitterMiner
from tweet_formatter import TweetFormatter
from tag_counter import TagCounter

@plac.annotations(
    keys=plac.Annotation("Twitter API keys", 'option', 'k', str),
    raw_tweets_file=plac.Annotation("TwitterMiner dump file", 'option', 'r',
                                    str),
    no_tweets=plac.Annotation("Number of tweets to download", 'option', 'n',
                              int),
    tracked_words_file=plac.Annotation("File with words to track", 'option',
                                       'w', str),
    formatted_tweets_file=plac.Annotation("convert2json dump file", 'option',
                                          'f', str),
    dictionaries=plac.Annotation("List of paths to dictionaries", 'option', 'd',
                                 list)
)
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

    counter = TagCounter(tagged_sents)
    res = counter.count()

    try:
        print("Palabras misóginas: {}".format(res['misóginia']))
    except KeyError:
        pass

    try:
        print("Palabras groseras: {}".format(res['grosería']))
    except KeyError:
        pass

if __name__ == '__main__':
    plac.call(main)
