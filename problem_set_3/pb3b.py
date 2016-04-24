# >>> secretWord = 'apple' 
# >>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# >>> print isWordGuessed(secretWord, lettersGuessed)
# False

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, 
    True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''

    for l in lettersGuessed:
        if (l in secretWord):
            secretWord = secretWord.replace(l, "")

    return len(secretWord) == 0

# print(isWordGuessed('apple', ['e', 'i', 'k', 'p', 'r', 's']))
# print(isWordGuessed('apple', ['a', 'p', 'l', 'e']))
