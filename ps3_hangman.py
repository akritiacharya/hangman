# Hangman
import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


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
    r=0
    for i in lettersGuessed:
        if i in secretWord:
            r +=1
    if r==len(secretWord):
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
    strreturn=''
    for i in secretWord:
        if i in lettersGuessed:
            strreturn +=i
        else:
            strreturn +='_'
    return strreturn



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    st=''
    letters='abcdefghijklmnopqrstuvwxyz'
    for i in letters:
        if not i in lettersGuessed:
            st = str(st) +str(i)
    return st
    

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
    print("Welcome to the game,Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long")
    print("-----------")
    round=8
    lettersGuessed=[]
    while round >=1:
        print("You have " + str(round) + " guesses left")
        print("Available letters :",getAvailableLetters(lettersGuessed))
        guess= str(input("Please guess a letter: "))
        if guess.lower() in lettersGuessed:
            print("Oops! You've already guessed that letter:",getGuessedWord(secretWord,lettersGuessed))
            round += 0
                    
        else:
            lettersGuessed.append(guess.lower())
            if guess.lower() not in secretWord:
                print("Oops! That letter isnot in my word:",getGuessedWord(secretWord,lettersGuessed))
                round -=1

            else:
                print("Good Guess:",getGuessedWord(secretWord,lettersGuessed))
                round +=0
                     
        print("-----------")  
        if '_' not in getGuessedWord(secretWord,lettersGuessed):
            print("Congratulations, you won!")
            break
                     
    if round <= 0:
        print("Sorry, you ran out of guesses. The word was " + str(secretWord)+ ".")
                     


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
