import yaml

class DictionaryTagger():

    def __init__(self, dictionary_paths):
        dictionaries = self.compile_dictionaries(dictionary_paths)
        self.dictionary = {}
        for curr_dict in dictionaries:
            for key in curr_dict:
                if key in self.dictionary:
                    self.dictionary[key].extend(curr_dict[key])
                else:
                    self.dictionary[key] = curr_dict[key]

    def compile_dictionaries(self, dictionary_paths):
        files = [open(path, "r") for path in dictionary_paths]
        dictionaries = [yaml.load(dict_file) for dict_file in files]
        for file in files:
            file.close()
        return dictionaries

    def tag(self, postagged_sentences):
        return [self.tag_sentence(sent) for sent in postagged_sentences]

    def tag_sentence(self, sentence, tag_with_lemmas=None):
        tagged_sentence = []
        for word in sentence:
            expression_form = word[0]
            literal = expression_form
            if literal in self.dictionary:
                tags = [tag for tag in self.dictionary[literal]]
                tags.append(word[1])
            else:
                tags = word[1]
            tagged_expression = (expression_form, tags)
            tagged_sentence.append(tagged_expression)

        return tagged_sentence
