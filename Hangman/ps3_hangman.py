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

WORDLIST_FILENAME = "/Users/Scure/Documents/6.00.1x Files/Hangman/words.txt"

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
    # FILL IN YOUR CODE HERE...
    #secretWord = 'hello'
    #lettersGuessed = ['a','d','s','h','e','l','o','h']
    
    if secretWord == '':
        return False
        
    if lettersGuessed == []:
        return False
    
    elif len(secretWord) != 0 and len(lettersGuessed) !=0 :
        count = 0 
        for i in secretWord:
            if i in lettersGuessed:
                count +=1
            
        if count == len(secretWord):
            return True
        else:
            return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...

    #secretWord = 'apple' 
    #lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    
    scList = []
    for i in secretWord:
        scList.append(i)
    
    newList = []
    for i in scList:
        if i in lettersGuessed:
            newList.append(i)
            
    guess=[]       
    for i in scList:
        if i in newList:
            guess.append(i)
        else:
            guess.append('_ ')
            
    global word
    word = ''
    for i in guess:
        word+=str(i)
    
    return word
        

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    aLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    newList = []
    if lettersGuessed == []:
        availableLetters = 'abcdefghijklmnopqrstuvwxyz'
        
    else:
        for i in aLetters:
            if i not in lettersGuessed:
                newList.append(i)
            
            
        availableLetters = ''
        for i in newList:
            availableLetters += str(i)    
        
    return availableLetters
    
def isInList(userInput, lettersGuessed):
    count = 0
    for i in lettersGuessed:
        if i == userInput:
            count +=1
    if count > 1:
        return True
    return
        
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
    # FILL IN YOUR CODE HERE...
    n = 8
    secretWord = secretWord.lower()
    global userInput
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is ' +str(len(secretWord)) + ' letters long'
    lettersGuessed = []
    
    
    #Loop hasta que la palabra sea adivinada
    
    while isWordGuessed(secretWord, lettersGuessed) == False:
        
            print 'You have ' +str(n)+ ' guesses left.'
            print 'Available Letters: '  + getAvailableLetters(lettersGuessed)
            userInput = raw_input('Please guess a letter: ')
            userInput = userInput.lower()
            lettersGuessed.append(userInput)
            
            
                
            if isInList(userInput, lettersGuessed) == True:
                print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
            elif userInput not in secretWord:
                print 'Oops! that letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed)
                n -=1
                if n == 0:
                    return 'You lost! the word was: ' + secretWord
            else:
                print 'Good guess: ' + getGuessedWord(secretWord, lettersGuessed)
        
    return 'Congratulations! you won, the word was: ' +secretWord
        
    
          
    
            
            
    
    





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

#secretWord = chooseWord(wordlist).lower()
#hangman(secretWord)
