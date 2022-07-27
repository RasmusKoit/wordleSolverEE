from typing import List, Dict, Set


def importFiveLetterWords(file_obj) -> Set:
    five_letter_words = set()
    with file_obj as f:
        for word in f:
            if len(word.strip()) == 5:
                five_letter_words.add(word.strip())
    return five_letter_words


# def certainLetters():
#
#
# def existingLetters():

def askForInput():
    matching_letters = int(input("Mitu tähte klapib, millel koht?"))
    found_letters = int(input("Mitu tähte leitud, millel puudub koht?"))
    wordle = {"found": []}
    for found in range(0, found_letters):
        letter = input("Sisesta täht")
        wordle["found"].append(letter)
    for matching in range(0, matching_letters):
        place = int(input("Mitmes täht"))
        letter = input("Sisesta täht")
        wordle[place - 1] = letter
    print(wordle)
    return wordle


def checkLetter(letter, position, word):
    if word[position] == letter:
        return True
    else:
        return False


def findInitialWords(user_guess: Dict, words):
    found_words = set()
    for letter in user_guess["found"]:
        for word in words:
            if letter in word:
                found_words.add(word)
    for position in range(0, 5):
        if position in user_guess:
            for word in words:
                if word[position] == user_guess[position]:
                    found_words.add(word)
    return found_words


def foundWordsRemover(words, user_guess):
    new_set = set()
    for letter in user_guess["found"]:
        for word in words:
            if letter in word:
                new_set.add(word)
    for letter in user_guess["found"]:
        for word in new_set.copy():
            if letter not in word:
                new_set.remove(word)
    return new_set


def foundWordsRemoverPlace(initialWords, guess):
    new_set = set()
    for word in initialWords:
        for number in range(0, 5):
            if number in guess:
                if checkLetter(guess[number], number, word):
                    new_set.add(word)
    for word in new_set.copy():
        for number in range(0, 5):
            if number in guess:
                if not checkLetter(guess[number], number, word):
                    if word in new_set:
                        new_set.remove(word)
    return new_set


if __name__ == '__main__':
    file_name = 'dictionary/lemmad.txt'
    file = open(file_name, 'r')
    words = importFiveLetterWords(file)
    guess = askForInput()
    initialWords = findInitialWords(guess, words)
    print(initialWords)
    if len(guess["found"]) > 0:
        print("l2ksin siia1")
        initialWords = foundWordsRemover(initialWords, guess)
    if any(isinstance(x, int) for x in guess):
        print("l2ksin siia2")
        initialWords = foundWordsRemoverPlace(initialWords, guess)
    print(initialWords)
