"""Word Finder: finds random words from a dictionary."""


import random


class WordFinder:
    """Find out how many words are in the file"""

    def __init__(self, words):
        dict = open(words)
        self.lines = self.parse(dict)
        print(f"There are a total of {len(self.lines)} words in this file.")

    """return a list of words available in the file"""

    def list(self):
        with open('dict_file.txt', 'r') as file:
            words = [w.strip() for w in file.read().split()]
            return words

    """find a random word in the file"""

    def random(self):
        return random.choice(self.lines)
