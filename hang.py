#! /usr/bin/python
import random
import string
import time
from os import system

WORDLIST_FILENAME = "words.txt"

class Archive:
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

class Word():

    secretWord = ''
    numberDifferentLetters = 0
    option = ''

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

def printLoadSituation(lenWordlist):
    print "Loading word list from file... Wait a few seconds, please"
    time.sleep(2)
    print lenWordlist, "words loaded."
    print "Press \033[91mENTER\033[0m to start"
    raw_input()

def printWelcomeMessage(secretWord, numberDifferentLetters):
    system("clear")
    print '\033[91mWelcome to the game, Hangam!\033[0m'
    print '\033[91mI am thinking of a word that is\033[33m', len(secretWord), '\033[0m\033[91mletters long.\033[0m'
    print '\033[91mThe word has\033[33m', numberDifferentLetters,'\033[0m\033[91mdifferent letters.\033[0m'
    print '-------------'
    print 'Lets get started...'
    print'\033[91m3\033[0m'
    time.sleep(1)
    print '\033[33m2\033[0m'
    time.sleep(1)
    print '1'

def isWordGuessed(secretWord, lettersGuessed):

    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False

    return True

def getGuessedWord():

     guessed = ''

     return guessed

def getAvailableLetters():
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase
    return available

def processLettersAvailable(lettersGuessed):
    available = getAvailableLetters()
    for letter in available:
        if letter in lettersGuessed:
            available = available.replace(letter, '')
    return available

def processGuess(string, lettersGuessed, secretWord):
    guessed = getGuessedWord()
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += ' _ '
    print string, guessed
    print '====================================================================='

def printResult(secretWord, lettersGuessed):
    system("clear")
    if isWordGuessed(secretWord, lettersGuessed) == True:
        print '==========================================='
        print '\033[92mCongratulations, you won! =)\033[0m '
        print 'The word was \033[45m', secretWord, '\033[0m.'
        print '==========================================='
    else:
        print '====================================================================='
        print '\033[92mSorry, you ran out of guesses =(\033[0m'
        print 'The word was \033[45m', secretWord, '\033[0m.'
        print '===================================================================='


def hangman(secretWord):
    guesses = 8
    lettersGuessed = []

    while  isWordGuessed(secretWord, lettersGuessed) == False and guesses > 0:
        print 'You have ', guesses, 'guesses left.'

        available = processLettersAvailable(lettersGuessed)
        print 'Available letters\033[33m', available,'\033[0m'

        letter = raw_input('\033[32mPlease guess a letter:\033[0m ')
        if letter in lettersGuessed:
            string = '\033[32mOops! You have already guessed that letter:\033[0m '

            processGuess(string, lettersGuessed, secretWord)

        elif letter in secretWord:
            lettersGuessed.append(letter)
            string = '\033[32mGood Guess:\033[0m '

            processGuess(string, lettersGuessed, secretWord)

        else:
            guesses -=1
            lettersGuessed.append(letter)
            string = '\033[32mOops! That letter is not in my word:\033[0m '

            processGuess(string, lettersGuessed, secretWord)

    else:
        printResult(secretWord, lettersGuessed)

archive = Archive(WORDLIST_FILENAME)
archive.openArchive()
archive.readArchive()
archive.makeListOfWords()
archive.calculateLengthOfWordlist()
printLoadSituation(archive.length)
word = Word()
word.chooseWord(archive.wordlist)
word.calculateDifferentLetters()
while word.chooseAnotherWord() == 1:
    word.chooseWord(archive.wordlist)
    word.calculateDifferentLetters()
printWelcomeMessage(word.secretWord, word.numberDifferentLetters)
hangman(word.secretWord)
