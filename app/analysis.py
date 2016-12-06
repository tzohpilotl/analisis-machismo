from dictionary_tagger import DictionaryTagger
from spaghetti import spaghetti as spgt
from twitter_miner import TwitterMiner

if __name__ == '__main__':

    miner = TwitterMiner('keys.ini', 'twitter_data.txt')
    miner.mine('tracks.csv')

    sent = 'Mi colega está embarazada por puta'.split()
    tagger = DictionaryTagger(['./misoginy_dictionary.yml'])
    postagged_sent = spgt.pos_tag(sent)    
    postagged_sentences = []
    postagged_sentences.append(postagged_sent)
    print(postagged_sent)

    spa_tagger = spgt.CESSTagger()
    unigram_tagger = spa_tagger.uni
    postagged_sent = unigram_tagger.tag(sent)
    postagged_sentences.append(postagged_sent)
    print(postagged_sent)

    tagged_sent = tagger.tag(postagged_sentences)
    print(tagged_sent)
    
