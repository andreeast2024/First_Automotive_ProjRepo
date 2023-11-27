import random

class WordGenerator:
    def __init__(self, filename="words.txt"):
        self.words = self.get_all_words(filename)

    def get_all_words(self, filename):
        try:
            with open(filename, "r") as file:
                return [line.strip().upper() for line in file.readlines()]
        except FileNotFoundError:
            print(f"Error: {filename} not found.")
            return []

    def get_random_word(self):
        if self.words:
            return random.choice(self.words)
        else:
            # Provide a default word if the file is empty or not found
            return "PYTHON"

class HangmanGame:
    def __init__(self, max_lives=6):
        self.max_lives = max_lives
        self.word_generator = WordGenerator()
        self.secret_word = self.word_generator.get_random_word()
        self.display_word = "_" * len(self.secret_word)
        self.guesses = []
        self.lives_left = max_lives

    def display_game_status(self):
        print(f"Current word: {self.display_word}")
        print(f"Lives left: {self.lives_left}")
        print(f"Guessed letters: {', '.join(self.guesses)}")

    def guess_letter(self, letter):
        letter = letter.upper()

        if letter in self.guesses:
            print(f"You've already guessed the letter {letter}. Try again.")
        else:
            self.guesses.append(letter)
            if letter in self.secret_word:
                print("Good guess!")
                self.update_display_word(letter)
            else:
                self.lives_left -= 1
                print("Incorrect guess")

    def is_game_over(self):
        return self.lives_left == 0 or "_" not in self.display_word

    def update_display_word(self, letter):
        for i, char in enumerate(self.secret_word):
            if char == letter:
                self.display_word = self.display_word[:i] + letter + self.display_word[i + 1:]

    def play(self):
        print("Welcome to Hangman!")

        while not self.is_game_over():
            self.display_game_status()
            user_input = input("Enter a letter: ")
            self.guess_letter(user_input)

        if "_" not in self.display_word:
            print(f"Congratulations! You guessed the word: {self.secret_word}")
        else:
            print(f"Game over! The word was: {self.secret_word}")
