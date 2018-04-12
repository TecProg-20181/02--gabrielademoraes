import string
from os import system

class Hangman:
    def __init__(self, secretWord):
        self.secretWord = secretWord
        self.lettersGuessed = []

    def isWordGuessed(self):
        for letter in self.secretWord:
            if letter in self.lettersGuessed:
                pass
            else:
                return False
        return True

    def getGuessedWord(self, string):
        guessed = ''
        for letter in self.secretWord:
            if letter in self.lettersGuessed:
                guessed += letter
            else:
                guessed += ' _ '
        print string, guessed
        print '====================================================================='

    def getAvailableLetters(self):
        # 'abcdefghijklmnopqrstuvwxyz'
        available = string.ascii_lowercase
        return available

    def processLettersAvailable(self):
        available = self.getAvailableLetters()
        for letter in available:
            if letter in self.lettersGuessed:
                available = available.replace(letter, '')
        return available

    def printResult(self):
        system("clear")
        if self.isWordGuessed() == True:
            print '==========================================='
            print '\033[92mCongratulations, you won! =)\033[0m '
            print 'The word was \033[45m', self.secretWord, '\033[0m.'
            print '==========================================='
        else:
            print '====================================================================='
            print '\033[92mSorry, you ran out of guesses =(\033[0m'
            print 'The word was \033[45m', self.secretWord, '\033[0m.'
            print '===================================================================='


    def hangman(self):
        guesses = 8

        while  self.isWordGuessed() == False and guesses > 0:
            print 'You have ', guesses, 'guesses left.'

            available = self.processLettersAvailable()
            print 'Available letters\033[33m', available,'\033[0m'

            letter = raw_input('\033[32mPlease guess a letter:\033[0m ')
            if letter in self.lettersGuessed:
                string = '\033[32mOops! You have already guessed that letter:\033[0m '

                self.getGuessedWord(string)

            elif letter in self.secretWord:
                self.lettersGuessed.append(letter)
                string = '\033[32mGood Guess:\033[0m '

                self.getGuessedWord(string)

            else:
                guesses -=1
                self.lettersGuessed.append(letter)
                string = '\033[32mOops! That letter is not in my word:\033[0m '

                self.getGuessedWord(string)

        else:
            self.printResult()
