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

    def test_tag_sentences(self):
        tagger = DictionaryTagger(['tests/subset_dict.yml',
                                   'tests/subset2_dict.yml'])
        postagged_sents = [[('Por', 'sps00'), ('perra', None), ('te', 'pp2cs000'), ('clavaré', None), ('este', 'dd0ms0'), ('fierro', None)], [('Aflojas', None), ('ote', None), ('corro,', None), ('pendeja', None)]]
        tagged_sents = [[('Por', 'sps00'), ('perra', ["machista"]), ('te', 'pp2cs000'), ('clavaré', None), ('este', 'dd0ms0'), ('fierro', None)], [('Aflojas', None), ('ote', None), ('corro,', None), ('pendeja', ["machista"])]]

        self.assertEqual(tagger.tag(postagged_sents), tagged_sents)
