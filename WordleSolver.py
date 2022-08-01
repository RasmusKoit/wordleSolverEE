from typing import List, Set
import re
from Word import Word


class Solver:
    length: int
    guesses: List[Word]
    words: Set[Word]
    guesses = []
    words = set()

    def __init__(self, words: Set[Word], length: int):
        self.length = length
        self.words = words

    def check_guess(self, guess: Word, feedback: str):
        name = guess.name
        for word in self.words.copy():
            for i in range(self.length):
                if feedback[i] == "w":
                    if len([index.start() for index in re.finditer(feedback[i], name)]) == 1 and name[i] in word.name:
                        self.words.remove(word)
                        break
                elif feedback[i] == "g" and name[i] != word.name[i]:
                    self.words.remove(word)
                    break
                elif feedback[i] == "y" and name[i] not in word.name:
                    self.words.remove(word)
                    break
                elif feedback[i] == "y" and name[i] == word.name[i]:
                    self.words.remove(word)
                    break

    def print_words_full(self):
        for word in self.words:
            print(word.description())

    def print_words_name(self):
        word_names = []
        for word in self.words:
            word_names.append(word.name)
        if len(self.words) == 0:
            self.final_results(0, "No more words found")
        print(", ".join(word_names))

    def enter_guess(self):
        while True:
            word_entry = Word(input("Enter a word: ").lower())
            if word_entry not in self.guesses:
                break
        feedback = input("Enter results: g: correct place, y: correct letter, w: doesn't exist, ex: gywww: \n")
        word_entry.color(feedback)
        self.guesses.append(word_entry)
        if feedback == "g" * self.length:
            self.final_results(0, "You won")
        self.check_guess(word_entry, feedback)

    def final_results(self, exit_code, exit_message):
        render = [" Results", (self.length + 4) * "─"]
        for guess in self.guesses:
            render.append("  " + guess.colored)
        for line in render:
            print(line)
        print(exit_message)
        exit(exit_code)

    def start(self):
        print("Welcome to wordle solver, some common words are:")
        sorted_words = list(sorted(self.words, reverse=True, key=lambda x: x.frequency))
        top_words = []
        for word in sorted_words[:10]:
            top_words.append(word.name)
        print(", ".join(top_words))
        for i in range(self.length):
            self.enter_guess()
            self.print_words_name()
        self.final_results(0, "Better luck next time")
