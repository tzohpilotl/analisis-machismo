from dictionary_tagger import DictionaryTagger
import spaghetti as spgt

if __name__ == '__main__':
    sent = 'Mi colega está embarazada por puta'.split()
    tagger = DictionaryTagger(['./d.yml'])
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
    
