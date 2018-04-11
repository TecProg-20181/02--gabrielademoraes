#! /usr/bin/python
import random
import string
import time
from os import system

WORDLIST_FILENAME = "palavras.txt"

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
        return self.inFile

    def readArchive(self):
        self.line = self.inFile.readline()

    def makeListOfWords(self):
        """
        Depending on the size of the word list, this function may
        take a while to finish.
        """
        self.wordlist = string.split(self.line)
        return self.wordlist

    def calculateLength(self):
        self.length = len(self.wordlist)

class Word():

    secretWord = ''
    numberDifferentLetters = 0

    def chooseWord(self, wordlist):
        self.secretWord = random.choice(wordlist).lower()

    def calculateDifferentLetters(self):
        repetitions = set(self.secretWord)
        self.numberDifferentLetters = len(repetitions)
        print self.numberDifferentLetters

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

def isWordGuessed(secretWord, lettersGuessed):
    secretLetters = []

#    for letter in secretWord:
#        if letter in secretLetters:
#            secretLetters.append(letter)
#        else:
#            pass

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
    print '------------'

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

def validateOption(option):
    while option != 'y' and option != 'n':
        print 'Invalid character! Try again'
        option = raw_input()

def chooseAnotherWord(secretWord, numberDifferentLetters):
    guesses = 8
    if guesses < numberDifferentLetters:#calculateDifferentLetters(secretWord):
        system("clear")
        print '\033[33mWARNING!\033[0m'
        print 'In the word drawn'
        print 'The number of different letters is higher than the number of guesses'
        print'Do you want to change the word ? [y/n]'
        option = raw_input()
        validateOption(option)
        if option == 'y':
            return 1
        return 2
    return 0

def hangman(secretWord):
    guesses = 8
    lettersGuessed = []

    while  isWordGuessed(secretWord, lettersGuessed) == False and guesses > 0:
        print 'You have ', guesses, 'guesses left.'

        available = processLettersAvailable(lettersGuessed)
        print 'Available letters\033[33m', available,'\033[0m'

        letter = raw_input('Please guess a letter: ')
        if letter in lettersGuessed:
            string = 'Oops! You have already guessed that letter: '

            processGuess(string, lettersGuessed, secretWord)

        elif letter in secretWord:
            lettersGuessed.append(letter)
            string = 'Good Guess: '

            processGuess(string, lettersGuessed, secretWord)

        else:
            guesses -=1
            lettersGuessed.append(letter)
            string = 'Oops! That letter is not in my word: '

            processGuess(string, lettersGuessed, secretWord)

    else:
        printResult(secretWord, lettersGuessed)


archive = Archive(WORDLIST_FILENAME)
archive.openArchive()
archive.readArchive()
archive.makeListOfWords()
archive.calculateLength()
printLoadSituation(archive.length)
word = Word()
word.chooseWord(archive.wordlist)
word.calculateDifferentLetters()
while chooseAnotherWord(word.secretWord, word.numberDifferentLetters) == 1:
    word.chooseWord(archive.wordlist)
printWelcomeMessage(word.secretWord, word.numberDifferentLetters)
hangman(word.secretWord)
