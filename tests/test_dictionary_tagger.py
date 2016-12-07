import unittest
from app.dictionary_tagger import DictionaryTagger

class TestDictionaryTagger(unittest.TestCase):

    def test_init_output(self):
        tagger = DictionaryTagger(['tests/subset_dict.yml'])
        d = {
            'puta': ['machista'],
            'estúpida': ['machista'],
            'pendeja': ['machista'],
            'zorra': ['machista'],
            'machorra': ['machista']
        }
        d2 = {
            'idiota': ['machista'],
            'madre': ['machista'],
            'maldita': ['machista'],
            'irresponsable': ['machista'],
            'deseosa': ['machista'],
            'perra': ['machista'],
            'tarada': ['machista']
        }
        self.assertEqual(tagger.
                             compile_dictionaries(['tests/subset_dict.yml']),
                             [d])
        self.assertEqual(tagger.
                             compile_dictionaries(['tests/subset_dict.yml'
                                                   ,'tests/subset2_dict.yml']),
                         [d,d2])        
