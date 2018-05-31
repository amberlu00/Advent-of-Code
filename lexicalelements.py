
sh_alphabetic_order = ['a', 'e', 'i', 'o', 'u', 'ai', 'au', \
                    'ei', 'eo', 'eu', 'y', 'w', \
                    'b', 'p', 'd', 't', 's', 'z', 'g', 'k', \
                    'n', 'm', 'r', 'l', 'h', 'sh', 'ch', 'ts', 'zh']

eng_alphabetic_order = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', \
                        'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', \
                        's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

class EntriesForLetter:
    def __init__(self, letter, pos):
        self.letter = letter
        self.dict = dict{}
    def get_dict(self):
        return self.dict
    def set_word(self, word, definition):
        self.dict["word"] = "definition"
    def check_word(self, word):
        if word in self.dict.keys():
            return True
    def get_definition(self, word):
        if self.check_word(word):
            return self.dict[word]
        else:
            return "This word doesn't exist, sorry."

class Entry:
    def __init__(self, root, stem, ipa, definition):
        self.root = root
        self.ipa = ipa
        self.stem = stem
        self.definition = definition

class Noun(Entry):
    def __init__(self):
        Entry.__init__(self)
        self.pos = "noun"
    def get_root(self):
        return self.root
    def get_stem(self):
        return self.stem
    def get_ipa(self):
        return self.ipa
    def get_pos(self):
        return self.pos

def add_noun(word, pos):
