import regex as regex

from Word import Word
from WordleSolver import Solver
from WordleGame import Game


class Wordle:
    words_file_path = 'dictionary/lemmad.txt'
    words_common_file_path = 'dictionary/common.txt'
    length = 5
    words = set()

    def __init__(self, length: int = 5):
        self.length = length
        self.words = set()

    def add_to_words(self, word_to_add: Word):
        if any(word.name == word_to_add.name for word in self.words):
            for word in self.words:
                if word.name == word_to_add.name:
                    word.set_frequency(word_to_add.frequency)
        else:
            self.words.add(word_to_add)

    def read_words_file(self, f_path: str, encoding: str):
        try:
            with open(f_path, encoding=encoding) as f:
                for line in f:
                    line = line.split()
                    if len(line[0]) == self.length:
                        if len(line) == 1:
                            self.add_to_words(Word(line[0].lower()))
                        elif len(line) > 4:
                            self.add_to_words(Word(line[0].lower(), int(line[2])))
        except FileNotFoundError:
            print(f"File: {f_path} not found")
        except IndexError:
            print(f"File: {f_path}, column does not exist on index")

    def select_mode(self):
        while True:
            response = input("Choose your mode: (solver, game) [solver]: ")
            if response == "" or response.lower() == "solver":
                self.read_words_file(self.words_file_path, "utf-8")
                self.read_words_file(self.words_common_file_path, "utf-8")
                return True
            elif response == "game":
                self.read_words_file(self.words_file_path, "utf-8")
                return False


w = Wordle()
if w.select_mode():
    solver = Solver(w.words, w.length)
    solver.start()
else:
    game = Game(w.words, w.length)
    game.start()

