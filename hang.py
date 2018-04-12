#! /usr/bin/python
import time
from os import system
from Classes.word import Word
from Classes.hangman import Hangman

WORDLIST_FILENAME = "words.txt"

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

def main():
    word = Word(WORDLIST_FILENAME)
    word.openArchive()
    word.readArchive()
    word.makeListOfWords()
    word.calculateLengthOfWordlist()
    printLoadSituation(word.length)
    word.chooseWord(word.wordlist)
    word.calculateDifferentLetters()
    while word.chooseAnotherWord() == 1:
        word.chooseWord(word.wordlist)
        word.calculateDifferentLetters()
    printWelcomeMessage(word.secretWord, word.numberDifferentLetters)
    game = Hangman(word.getSecretWord())
    game.hangman()

main()
