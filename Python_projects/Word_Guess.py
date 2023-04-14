import random

class WordGuess:
    def __init__(self, words):
        self.words = words
        self.word = ""
        self.guesses = []
        self.max_guesses = 6

    def start(self):
        self.word = random.choice(self.words).lower()
        self.guesses = []
        print("Welcome to Word Guess!")
        print(f"The word is {len(self.word)} letters long.")
        self.print_hidden_word()

        while not self.game_over():
            guess = input("Guess a letter: ").lower()
            if guess in self.guesses:
                print("You already guessed that letter.")
            else:
                self.guesses.append(guess)
                if guess in self.word:
                    print("Correct!")
                    self.print_hidden_word()
                else:
                    print("Incorrect.")
                    self.print_hidden_word()
                    print(f"You have {self.max_guesses - len(self.guesses)} guesses left.")

        if self.word_guessed():
            print("Congratulations, you guessed the word!")
        else:
            print(f"Sorry, you ran out of guesses. The word was '{self.word}'.")

    def print_hidden_word(self):
        hidden_word = ""
        for letter in self.word:
            if letter in self.guesses:
                hidden_word += letter
            else:
                hidden_word += "_"
        print(hidden_word)

    def word_guessed(self):
        for letter in self.word:
            if letter not in self.guesses:
                return False
        return True

    def game_over(self):
        if self.word_guessed():
            return True
        elif len(self.guesses) >= self.max_guesses:
            return True
        else:
            return False

words = ["apple", "banana", "cherry", "durian", "elderberry"]
game = WordGuess(words)
game.start()
