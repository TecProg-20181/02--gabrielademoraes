#! /usr/bin/python
import random
import string
import time
from os import system

WORDLIST_FILENAME = "words.txt"

def openArchive():
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    return inFile

def readArchive(inFile):
    line = inFile.readline()
    return line

def makeListOfWords(line):
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    wordlist = string.split(line)
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)

def printLoadSituation(wordlist):
    print "Loading word list from file... Wait a few seconds, please"
    time.sleep(2)
    print len(wordlist), "words loaded."
    print "Press \033[91mENTER\033[0m to start"
    raw_input()

def printWelcomeMessage(secretWord):
    system("clear")
    print '\033[91mWelcome to the game, Hangam!\033[0m'
    print '\033[91mI am thinking of a word that is', len(secretWord), ' letters long.\033[0m'
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

# inFile: file
inFile = openArchive()
# line: string
line = readArchive(inFile)
# wordlist: list of strings
wordlist = makeListOfWords(line)
printLoadSituation(wordlist)
secretWord = chooseWord(wordlist).lower()
printWelcomeMessage(secretWord)
hangman(secretWord)
