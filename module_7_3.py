class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    punct = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for symbol in punct:
                        line = line.replace(symbol, '')
                    words.extend(line.split())
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word_positions = {}
        word = word.lower()
        for file_name, words in self.get_all_words().items():
            if word in words:
                return {file_name: words.index(word) + 1}
            else:
                return word_positions

    def count(self, word):
        word_count = {}
        word = word.lower()
        for file_name, words in self.get_all_words().items():
            word_count[file_name] = words.count(word)
        return word_count


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего