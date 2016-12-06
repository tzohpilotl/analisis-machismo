import unittest
from app import readkeys as rk

class TestReadKeys(unittest.TestCase):

    def setup(self):
        pass

    def test_missingSection(self):
        self.assertRaises(LookupError, rk.readKeys, './tests/keys1.ini')

    def test_validFiles(self):
        correct_keys = {
            'access_token': '3265482518-jdsSS32',
            'access_token_secret': 'EWFzf8x5KtgYVLsld223dDpdm7leTra',
            'consumer_key': '92RNpQg5Mm11DsdDG',
            'consumer_secret': 'lsSD34EesdF52'
        }
        self.assertEqual(rk.readKeys('./tests/keys2.ini'), correct_keys)
        self.assertEqual(rk.readKeys('./tests/keys3.ini'), correct_keys)

if __name__ == '__main__':
    unittest.main()
