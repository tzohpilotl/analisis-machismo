import unittest
from app.key_reader import KeyReader

class TestKeyReader(unittest.TestCase):

    def setup(self):
        pass

    def test_missing_section(self):
        kr = KeyReader()
        self.assertRaises(LookupError, kr.read, './tests/keys1.ini')

    def test_valid_files(self):
        correct_keys = {
            'access_token': '3265482518-jdsSS32',
            'access_token_secret': 'EWFzf8x5KtgYVLsld223dDpdm7leTra',
            'consumer_key': '92RNpQg5Mm11DsdDG',
            'consumer_secret': 'lsSD34EesdF52'
        }
        kr = KeyReader()
        self.assertEqual(kr.read('./tests/keys2.ini'), correct_keys)
        self.assertEqual(kr.read('./tests/keys3.ini'), correct_keys)

if __name__ == '__main__':
    unittest.main()
