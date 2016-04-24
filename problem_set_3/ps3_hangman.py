# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''

    for l in lettersGuessed:
        if (l in secretWord):
            secretWord = secretWord.replace(l, "")

    return len(secretWord) == 0


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    word = secretWord
    for l in lettersGuessed:
        if (l in secretWord):
            word = word.replace(l, '')

    for l in word:
        if (l in secretWord):
            secretWord = secretWord.replace(l, '_ ')

    return secretWord


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    alph = string.ascii_lowercase

    for l in lettersGuessed:
        if (l in alph):
            alph = alph.replace(l, '')

    return alph  
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is %i letters long' % len(secretWord)
    guesses = 8
    lettersGuessed = []
    while (guesses):
        print '-------------'
        print 'You have %i guesses left' % guesses
        print 'Available letters: %s' % getAvailableLetters(lettersGuessed)
        letter = raw_input('Please guess a letter: ')
        if (letter in lettersGuessed):
            print 'You already guessed that letter'
        else:
            lettersGuessed.append(letter)

            if (letter in secretWord):
                print 'Good guess: %s' % getGuessedWord(secretWord, lettersGuessed)
            else:
                guesses -= 1
                print 'Opps! You out of luck son: %s' % getGuessedWord(secretWord, lettersGuessed)

            if (isWordGuessed(secretWord, lettersGuessed)):
                print 'Congratulations, you won! Have a nice day.'
                break
            elif (guesses == 0):
                print 'The word was %s. AI reigns supreme.' % secretWord


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
