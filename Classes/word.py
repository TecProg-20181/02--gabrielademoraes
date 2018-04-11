import string
import random
from os import system

class Word():

    secretWord = ''
    numberDifferentLetters = 0
    option = ''
    fileName = ''
    inFile = ''
    line = ''
    wordlist = ''
    length = 0

    def __init__(self, fileName):
        self.fileName = fileName

    def openArchive(self):
        self.inFile = open(self.fileName, 'r', 0)

    def readArchive(self):
        self.line = self.inFile.readline()

    def makeListOfWords(self):
        """
        Depending on the size of the word list, this function may
        take a while to finish.
        """
        self.wordlist = string.split(self.line)

    def calculateLengthOfWordlist(self):
        self.length = len(self.wordlist)

    def chooseWord(self, wordlist):
        self.secretWord = random.choice(wordlist).lower()

    def calculateDifferentLetters(self):
        repetitions = set(self.secretWord)
        self.numberDifferentLetters = len(repetitions)

    def chooseAnotherWord(self):
        guesses = 8
        if guesses < self.numberDifferentLetters:
            system("clear")
            print '\033[33mWARNING!\033[0m'
            print 'In the word drawn'
            print 'The number of different letters is higher than the number of guesses'
            print '\033[92mIf you would like to change, sometimes you will have to press yes more than once until the system draw a word that fits\033[0m'
            print'Do you want to change the word ? [y/n]'
            self.option = raw_input()
            self.validateOption()
            if self.option == 'y':
                return 1
            return 2
        return 0

    def validateOption(self):
        while self.option != 'y' and self.option != 'n':
            print 'Invalid character! Try again'
            self.option = raw_input()

    def getSecretWord(self):
            return self.secretWord
