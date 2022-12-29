import os.path
import nltk


class FileReader:
    def __init__(self, path):
        self.path = path
        if not os.path.exists(self.path) or not os.path.isfile(self.path):
            self.exist = False
        else:
            self.exist = True
        self.line_count = None
        self.word_count = None

    def read(self):
        if not self.exist:
            return ''
        with open(self.path, "r") as file:
            return file.read()

    def write(self, text):
        if not self.exist:
            return
        with open(self.path, "a") as file:
            file.write(text)

    def count(self):
        if self.line_count is None:
            self.line_count = len(self.read().split('\n'))
        if self.word_count is None:
            self.word_count = len(nltk.word_tokenize(self.read()))
        return self.line_count, self.word_count

    def __add__(self, other):
        if self.exist and other.exist:
            new_path = f"{os.path.basename(self.path)}_and_{os.path.basename(other.path)}"
            with open(new_path, "w") as new:
                new.write(self.read() + other.read())
            return FileReader(new_path)

    def __str__(self):
        return os.path.abspath(self.path)

    
