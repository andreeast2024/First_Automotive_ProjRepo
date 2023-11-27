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