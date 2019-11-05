class MyWords:
    def __init__(self, file: str, substring: str):
        self.substring = substring
        with open(file, 'r') as mf:
            self.my_file = mf.readlines()
        self.my_iter = iter(self.my_file)

    def __iter__(self):
        return self

    def __next__(self):
        next_el = next(self.my_iter)
        if not next_el:
            raise StopIteration
        return next_el

    def __str__(self):
        return str(self.my_file)

    def get_words_with_sub(self):
        for line in self.my_file:
            for word in line.split(','):
                if self.substring in word:
                    yield word.replace(self.substring, self.substring.upper())


if __name__ == "__main__":
    substring_finder = MyWords("file_with_words.txt", "kaf")
    print(list(substring_finder.get_words_with_sub()))

