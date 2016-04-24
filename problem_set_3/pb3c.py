# >>> secretWord = 'apple' 
# >>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# >>> print getGuessedWord(secretWord, lettersGuessed)
# '_ pp_ e'

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word = secretWord
    for l in lettersGuessed:
        if (l in secretWord):
            word = word.replace(l, '')

    for l in word:
        if (l in secretWord):
            secretWord = secretWord.replace(l, '_ ')

    return secretWord

# print(getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's']))