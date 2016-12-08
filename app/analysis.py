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
    """Perform an analyisis to find sexist and rude words in tweets

    This module employs every other module to perform a full analysis on data
    retrieved from the Twitter stream. First a TwitterMiner retrieves data and
    dumps it, then a TweetFormatter parses the data into a list of tweets that
    are lists of words. Then it uses the spaghetti tagger to POStag every word,
    yielding a list of tweets that are lists with elements with the form (word,
    [tags]). A DictionaryTagger adds our custom tags to the [tags] list. Finally
    a TagCounter perform a count of every tag found in tweets. This program 
    prints the number of coincidences of our custom tags.
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
