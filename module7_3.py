class WordsFinder:
    def __init__(self,*args):
        self.file_names = []
        for i in args:
            self.file_names.append(i)

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                words_in_file = ''
                for line in file:
                    words_in_file += line
                words_in_file = words_in_file.replace(',', '').replace('.', '')
                words_in_file = words_in_file.replace('=', '').replace('!', '')
                words_in_file = words_in_file.replace('?', '').replace(';', '')
                words_in_file = words_in_file.replace(':', '').replace(' - ', ' ')
                words_in_file = words_in_file.lower().split()
                all_words[i] = words_in_file
        return all_words

    def find(self, word):
        find_out = {}
        words = self.get_all_words()
        for key in words:
            n = 0
            for i in words[key]:
                n += 1
                if word.lower() == i:
                    find_out[key] = n
                    break
        return find_out


    def count(self, word):
        count_out = {}
        words = self.get_all_words()
        for key in words:
            n = 0
            for i in words[key]:
                if word.lower() == i:
                    n += 1
            count_out[key] = n
        return count_out


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
