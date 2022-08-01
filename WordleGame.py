from typing import Set, List
from random import choice
from Word import Word


class Game:
    words: Set[Word]
    words = set()
    word: Word
    length: int
    guesses: List[Word]

    def __init__(self, words: Set[Word], length: int):
        self.length = length
        self.words = words
        self.word = choice(list(self.words))
        self.guesses = []
        # print(self.word.name)

    def start(self):
        for i in range(self.length):
            self.ask_user()
            self.print_guesses()
        print(f"You lost, correct word was: {self.word.name}")

    def print_guesses(self):
        for guess in self.guesses:
            print(guess.colored)

    def ask_user(self) -> str:
        result = input(f"Please enter a {str(self.length)} letter word: ")
        print(result)
        feedback = self.get_feedback(result)
        self.guesses.append(feedback)

    def get_feedback(self, result: str) -> Word:
        feedback = ""
        for i in range(len(result)):
            if result[i] not in self.word.name:
                feedback += 'w'
            elif result[i] == self.word.name[i]:
                feedback += 'g'
            elif result[i] in self.word.name:
                feedback += 'y'
                # r_count = result.count(result[i])
                # w_count = self.word.name.count(result[i])
                # if r_count == w_count:
                #     feedback += 'y'
                # elif r_count < w_count and i < self.word.name.index(result[i]):
                #     feedback += 'y'
                # else:
                #     feedback += 'w'
        self.has_won(feedback)
        return Word(result, feedback=feedback)

    def has_won(self, feedback):
        if feedback == self.length*"g":
            print("You have won!")
            exit(0)
