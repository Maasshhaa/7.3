class WordsFinder:
    def __init__(self, *name):
        self.file_names = name

    def get_all_words(self):
        blacklist = [',', '.', '=', '!', '?', ';', ':', ' - ', '\n']
        all_worlds = {}
        for name in self.file_names:
            word = []
            with open(name, encoding='utf-8') as file:
                for line in file:
                    line = line.lower()

                    for punctuation in blacklist:
                        if punctuation in line:
                            line = line.replace(punctuation, '')

                    line = line.split()
                    for worlds in line:
                        word.append(worlds)
            all_worlds[name] = word
        return all_worlds

    def count(self, word):
        found = {}
        for name in self.file_names:
            quantity = 0
            list_world = self.get_all_words().get(name)
            for item in list_world:
                if item == word:
                    quantity += 1
                found[name] = quantity
        return found

    def find(self, word):
        found = {}
        for name in self.file_names:
            position = 0
            list_world = self.get_all_words().get(name)
            for item in list_world:
                position += 1
                if item == word:
                    found[name] = position
        return found


finder = WordsFinder('sing.txt', 'txt.txt')
print(finder.get_all_words())
print(finder.find('our'))
print(finder.count('our'))
