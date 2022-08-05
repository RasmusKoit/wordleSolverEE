from typing import Set, List
from random import choice
from Word import Word
from re import finditer

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
        print(self.word.name)

    def start(self):
        for i in range(self.length):
            self.ask_user()
            self.print_guesses()
        print(f"You lost, correct word was: {self.word.name}")

    def print_guesses(self):
        for guess in self.guesses:
            print(guess.colored)

    def ask_user(self):
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
                r_indices = [j.start() for j in finditer(result[i], result)]
                w_indices = [j.start() for j in finditer(result[i], self.word.name)]
                feedback_count = 0
                for r in range(len(r_indices)):
                    if r_indices[r] < i:
                        if feedback[r_indices[r]] == 'y' or feedback[r_indices[r]] == 'g':
                            feedback_count += 1
                if feedback_count < len(w_indices):
                    feedback += 'y'
                else:
                    feedback += 'w'
                print(r_indices, w_indices, i)

        self.has_won(feedback)
        return Word(result, feedback=feedback)

    def has_won(self, feedback):
        if feedback == self.length*"g":
            print("You have won!")
            exit(0)
