# >>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# >>> print getAvailableLetters(lettersGuessed)
# abcdfghjlmnoqtuvwxyz

import string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alph = string.ascii_lowercase

    for l in lettersGuessed:
        if (l in alph):
            alph = alph.replace(l, '')

    return alph    

# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print getAvailableLetters(lettersGuessed) == 'abcdfghjlmnoqtuvwxyz'
