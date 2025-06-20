import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)

def isWordGuessed(secretWord, lettersGuessed):
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    output = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            output += letter
        else:
            output += " _ "
    return output

def getAvailableLetters(lettersGuessed):
    output = ""
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            output += letter
    return output

def autoPlay(secretWord):
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', len(secretWord), 'letters long.')
    print('-------------')
    
    mistakesMade = 0
    lettersGuessed = []
    
    # Common letter frequency in English
    letter_frequency = 'etaoinshrdlcumwfgypbvkjxqz'
    
    while mistakesMade < 8 and not isWordGuessed(secretWord, lettersGuessed):
        print('You have', 8 - mistakesMade, 'guesses left.')
        print('Available letters:', getAvailableLetters(lettersGuessed))
        
        # Auto-select a letter based on frequency
        for letter in letter_frequency:
            if letter not in lettersGuessed:
                guess = letter
                break
        
        print(f'Computer guesses letter: {guess}')
        lettersGuessed.append(guess)
        
        if guess in secretWord:
            print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
        else:
            print('Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
            mistakesMade += 1
        
        print('------------')
    
    if isWordGuessed(secretWord, lettersGuessed):
        print('Congratulations, the computer won!')
    else:
        print('Sorry, the computer ran out of guesses. The word was', secretWord + '.')

# Load words and play
wordlist = loadWords()
secretWord = chooseWord(wordlist).lower()
print(f"\n[AUTO-PLAY MODE: The secret word is '{secretWord}']\n")
autoPlay(secretWord)