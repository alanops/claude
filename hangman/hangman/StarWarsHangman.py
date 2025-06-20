# Star Wars Themed Hangman Game
import random

WORDLIST_FILENAME = "star_wars_words.txt"

def loadWords():
    """
    Returns a list of valid Star Wars words.
    """
    print("\n=== STAR WARS HANGMAN ===")
    print("A long time ago in a galaxy far, far away...")
    print("\nLoading the Jedi archives...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(f"  {len(wordlist)} entries found in the archives.")
    print("May the Force be with you!\n")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
wordlist = loadWords()

def displayHangman(mistakes):
    """
    Display Star Wars themed hangman stages
    """
    stages = [
        # 0 mistakes
        """
           _____
          |     |
          |     
          |    
          |    
          |
        ===== 
        """,
        # 1 mistake
        """
           _____
          |     |
          |     O
          |    
          |    
          |
        ===== 
        """,
        # 2 mistakes
        """
           _____
          |     |
          |     O
          |     |
          |    
          |
        ===== 
        """,
        # 3 mistakes
        """
           _____
          |     |
          |     O
          |    /|
          |    
          |
        ===== 
        """,
        # 4 mistakes
        """
           _____
          |     |
          |     O
          |    /|\\
          |    
          |
        ===== 
        """,
        # 5 mistakes
        """
           _____
          |     |
          |     O
          |    /|\\
          |    /
          |
        ===== 
        """,
        # 6 mistakes
        """
           _____
          |     |
          |     O
          |    /|\\
          |    / \\
          |
        ===== 
        DANGER: The Dark Side grows stronger!
        """,
        # 7 mistakes
        """
           _____
          |     |
          |     X
          |    /|\\
          |    / \\
          |
        ===== 
        The Empire has won...
        """
    ]
    print(stages[mistakes])

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            result += letter + ' '
        else:
            result += '_ '
    return result.strip()


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    available = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        if letter in available:
            available.remove(letter)
    return ''.join(available)

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Star Wars Hangman.
    '''
    print("╔════════════════════════════════════════╗")
    print("║     Welcome, young Padawan!            ║")
    print("║  The Jedi Council has a test for you.  ║")
    print("╚════════════════════════════════════════╝")
    print(f"\nI sense a presence... a word with {len(secretWord)} letters.")
    print("You must use the Force to reveal it before the Empire captures you!")
    print("You have 8 attempts before you fall to the Dark Side.\n")
    
    mistakesMade = 0
    lettersGuessed = []
    
    while mistakesMade < 8:
        
        if isWordGuessed(secretWord, lettersGuessed):
            print("\n" + "="*50)
            print("🌟 The Force is strong with you! 🌟")
            print(f"You have discovered: {secretWord.upper()}")
            print("The Jedi Council welcomes you as a Knight!")
            print("="*50)
            break
            
        else:
            displayHangman(mistakesMade)
            print("-" * 50)
            print(f"Attempts remaining: {8 - mistakesMade}")
            print(f"Available letters: {getAvailableLetters(lettersGuessed)}")
            print(f"Current word: {getGuessedWord(secretWord, lettersGuessed)}")
            
            guess = str(input("\nUse the Force, choose a letter: ")).lower()
            
            if len(guess) != 1 or not guess.isalpha():
                print("⚠️  Invalid input! Please enter a single letter.")
                continue
                
            if guess in lettersGuessed:
                print(f"💫 You've already sensed that letter: {getGuessedWord(secretWord, lettersGuessed)}")
                
            elif guess in secretWord:
                lettersGuessed.append(guess)
                print(f"✨ Well done! The Force guides you: {getGuessedWord(secretWord, lettersGuessed)}")
                
            else:
                lettersGuessed.append(guess)
                mistakesMade += 1
                print(f"💀 The Dark Side clouds your vision: {getGuessedWord(secretWord, lettersGuessed)}")
                
        if mistakesMade == 8:
            displayHangman(7)
            print("\n" + "="*50)
            print("💔 You have fallen to the Dark Side...")
            print(f"The word was: {secretWord.upper()}")
            print("The Empire has won this battle.")
            print("="*50)
            break

# ASCII Art for intro
def showIntro():
    print("""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⣷⣶⣤⣀⠀⠀⠀⠀
    ⠀⠀⠀⣠⣴⣿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣦⣄⠀
    ⠀⢠⣾⡿⠋⠀⠀⠀⠀⠀⠀⠀ STAR WARS ⠀⠀⠀⠀⠀⠀⠀⠙⢿⣷⡄
    ⢠⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⡄
    ⣾⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  HANGMAN  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣷
    ⢿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡿
    ⠈⢿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⡿⠁
    ⠀⠀⠙⢿⣷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⡿⠋⠀⠀
    ⠀⠀⠀⠀⠈⠙⠻⠿⣿⣶⣶⣤⣤⣤⣤⣤⣤⣤⣤⣤⣶⣶⣿⠿⠟⠋⠁⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠛⠛⠛⠛⠛⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """)

# Main game execution
showIntro()
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)