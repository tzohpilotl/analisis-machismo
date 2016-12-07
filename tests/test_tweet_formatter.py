import unittest
from app.tweet_formatter import TweetFormatter

class TestTweetFormatter(unittest.TestCase):

    def test_inexistentFile(self):
        f = TweetFormatter('ghost_file.txt')
        f2 = TweetFormatter()
        self.assertRaises(FileNotFoundError, f.convert2json)
        self.assertRaises(ValueError, f2.convert2json)
        self.assertRaises(FileNotFoundError, f.convert2json, 'ghost_file.txt')
        self.assertRaises(FileNotFoundError, f2.convert2json, 'ghost_file.txt')

    def test_noJSONTweets(self):
        f = TweetFormatter()
        ghost_tweets = {}
        self.assertRaises(ValueError, f.convert2text)
        self.assertEqual(f.convert2text(ghost_tweets), [])
        f2 = TweetFormatter()
        ghost_tweets = None
        self.assertRaises(ValueError, f.convert2text)
        self.assertRaises(ValueError, f.convert2text, ghost_tweets)

    def test_noTextTweets(self):
        f = TweetFormatter('tests/ghost_file.txt')
        ghost_text = []
        self.assertRaises(ValueError, f.clean_tweets)
        self.assertEqual(f.clean_tweets(ghost_text), [])
        f2 = TweetFormatter()
        self.assertRaises(ValueError, f.clean_tweets)
        self.assertEqual(f.clean_tweets(ghost_text), [])

    def test_noTextKey(self):
        f = TweetFormatter('tests/no_text.txt')
        no_text_tweet = f.convert2json()
        self.assertEqual(f.convert2text(no_text_tweet), [])

if __name__ == '__main__':
    unittest.main()
