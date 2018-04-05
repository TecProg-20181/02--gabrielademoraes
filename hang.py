#! /usr/bin/python
import random
import string
import time
from os import system

WORDLIST_FILENAME = "palavras.txt"

def openArchive():
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    return inFile

def readArchive(inFile):
    line = inFile.readline()
    return line

def makeListOfWords(line):
    wordlist = string.split(line)
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)

def printLoadSituation(wordlist):
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    time.sleep(2)
    print len(wordlist), "words loaded."
    print "Press ENTER to start"
    raw_input()

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
    import string
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase
    return available

def hangman(secretWord):
    guesses = 8
    lettersGuessed = []
    system("clear")
    print 'Welcome to the game, Hangam!'
    print 'I am thinking of a word that is', len(secretWord), ' letters long.'
    print '-------------'
    time.sleep(2)
    while  isWordGuessed(secretWord, lettersGuessed) == False and guesses >0:
        print 'You have ', guesses, 'guesses left.'

        available = getAvailableLetters()
        for letter in available:
            if letter in lettersGuessed:
                available = available.replace(letter, '')

        print 'Available letters', available
        letter = raw_input('Please guess a letter: ')
        if letter in lettersGuessed:

            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Oops! You have already guessed that letter: ', guessed
        elif letter in secretWord:
            lettersGuessed.append(letter)

            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Good Guess: ', guessed
        else:
            guesses -=1
            lettersGuessed.append(letter)

            guessed = getGuessedWord()
            for letter in secretWord:
                if letter in lettersGuessed:
                    guessed += letter
                else:
                    guessed += '_ '

            print 'Oops! That letter is not in my word: ',  guessed
        print '------------'
    else:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was \033[45m', secretWord, '\033[0m .'

# inFile: file
inFile = openArchive()
# line: string
line = readArchive(inFile)
# wordlist: list of strings
wordlist = makeListOfWords(line)
printLoadSituation(wordlist)
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
