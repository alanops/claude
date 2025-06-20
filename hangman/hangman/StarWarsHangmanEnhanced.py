# Enhanced Star Wars Themed Hangman Game
import random
import time

WORDLIST_FILENAME = "star_wars_words.txt"

# Star Wars character quotes for different game events
YODA_QUOTES = [
    "Do or do not, there is no try.",
    "The greatest teacher, failure is.",
    "Much to learn, you still have.",
    "Patience you must have, my young Padawan."
]

VADER_QUOTES = [
    "I find your lack of faith disturbing.",
    "You don't know the power of the Dark Side.",
    "The Force is strong with this one.",
    "Your skills are complete."
]

OBI_WAN_QUOTES = [
    "The Force will be with you, always.",
    "These aren't the droids you're looking for.",
    "In my experience, there's no such thing as luck.",
    "Your eyes can deceive you; don't trust them."
]

def loadWords():
    """
    Returns a list of valid Star Wars words.
    """
    print("\n" + "="*60)
    print("     ███████╗████████╗ █████╗ ██████╗     ██╗    ██╗ █████╗ ██████╗ ███████╗")
    print("     ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗    ██║    ██║██╔══██╗██╔══██╗██╔════╝")
    print("     ███████╗   ██║   ███████║██████╔╝    ██║ █╗ ██║███████║██████╔╝███████╗")
    print("     ╚════██║   ██║   ██╔══██║██╔══██╗    ██║███╗██║██╔══██║██╔══██╗╚════██║")
    print("     ███████║   ██║   ██║  ██║██║  ██║    ╚███╔███╔╝██║  ██║██║  ██║███████║")
    print("     ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝     ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝")
    print("                           H A N G M A N")
    print("="*60)
    
    print("\nA long time ago in a galaxy far, far away...")
    time.sleep(1)
    print("\nAccessing the Jedi Archives...")
    
    # inFile: file
    try:
        inFile = open(WORDLIST_FILENAME, 'r')
        line = inFile.readline()
        wordlist = line.split()
        inFile.close()
        print(f"✓ {len(wordlist)} entries loaded from the holocron.")
        print("\n" + random.choice(OBI_WAN_QUOTES))
        return wordlist
    except:
        print("Error: Could not access the Jedi Archives!")
        return ["luke", "vader", "yoda", "leia", "force"]

def chooseWord(wordlist):
    """
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

def displayLightsaber(mistakes):
    """
    Display lightsaber-themed hangman stages
    """
    stages = [
        # 0 mistakes - Full lightsaber
        """
        ╔═══════════════════════════════╗
        ║      LIGHTSABER STATUS        ║
        ╠═══════════════════════════════╣
        ║            |===|              ║
        ║            |===|              ║
        ║            |===|              ║
        ║            |===|              ║
        ║            |===|              ║
        ║            [___]              ║
        ║         FULL POWER            ║
        ╚═══════════════════════════════╝
        """,
        # 1 mistake
        """
        ╔═══════════════════════════════╗
        ║      LIGHTSABER STATUS        ║
        ╠═══════════════════════════════╣
        ║            |===|              ║
        ║            |===|              ║
        ║            |===|              ║
        ║            |===|              ║
        ║            [___]              ║
        ║         87% POWER             ║
        ╚═══════════════════════════════╝
        """,
        # 2 mistakes
        """
        ╔═══════════════════════════════╗
        ║      LIGHTSABER STATUS        ║
        ╠═══════════════════════════════╣
        ║            |===|              ║
        ║            |===|              ║
        ║            |===|              ║
        ║            [___]              ║
        ║         75% POWER             ║
        ╚═══════════════════════════════╝
        """,
        # 3 mistakes
        """
        ╔═══════════════════════════════╗
        ║      LIGHTSABER STATUS        ║
        ╠═══════════════════════════════╣
        ║            |===|              ║
        ║            |===|              ║
        ║            [___]              ║
        ║         62% POWER             ║
        ╚═══════════════════════════════╝
        """,
        # 4 mistakes
        """
        ╔═══════════════════════════════╗
        ║      LIGHTSABER STATUS        ║
        ╠═══════════════════════════════╣
        ║            |===|              ║
        ║            [___]              ║
        ║         50% POWER             ║
        ║      ⚠️  WARNING ⚠️           ║
        ╚═══════════════════════════════╝
        """,
        # 5 mistakes
        """
        ╔═══════════════════════════════╗
        ║      LIGHTSABER STATUS        ║
        ╠═══════════════════════════════╣
        ║            |=|                ║
        ║            [_]                ║
        ║         37% POWER             ║
        ║      🔴 CRITICAL 🔴           ║
        ╚═══════════════════════════════╝
        """,
        # 6 mistakes
        """
        ╔═══════════════════════════════╗
        ║      LIGHTSABER STATUS        ║
        ╠═══════════════════════════════╣
        ║            [_]                ║
        ║         25% POWER             ║
        ║    💀 FAILING 💀              ║
        ╚═══════════════════════════════╝
        """,
        # 7 mistakes
        """
        ╔═══════════════════════════════╗
        ║      LIGHTSABER STATUS        ║
        ╠═══════════════════════════════╣
        ║            [ ]                ║
        ║         12% POWER             ║
        ║   ☠️  LAST CHANCE ☠️          ║
        ╚═══════════════════════════════╝
        """,
        # 8 mistakes - Game Over
        """
        ╔═══════════════════════════════╗
        ║      LIGHTSABER STATUS        ║
        ╠═══════════════════════════════╣
        ║            XXX                ║
        ║         0% POWER              ║
        ║    ⚫ EXTINGUISHED ⚫         ║
        ║                               ║
        ║    THE DARK SIDE WINS         ║
        ╚═══════════════════════════════╝
        """
    ]
    print(stages[mistakes])

def isWordGuessed(secretWord, lettersGuessed):
    '''
    Returns True if all letters of secretWord are in lettersGuessed
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    Returns the word with guessed letters revealed
    '''
    result = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            result += letter.upper() + ' '
        else:
            result += '_ '
    return result.strip()

def getAvailableLetters(lettersGuessed):
    '''
    Returns letters that haven't been guessed yet
    '''
    import string
    available = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        if letter in available:
            available.remove(letter)
    return ''.join(available)

def getRandomQuote(quotes):
    '''
    Returns a random quote from the given list
    '''
    return random.choice(quotes)

def showCharacterArt():
    '''
    Shows random Star Wars character ASCII art
    '''
    arts = [
        # Yoda
        """
                    ____
                 _.' :  `._
             .-.'`.  ;   .'`.-.
            (__  \ \ ; / /  __)
             ) )  '.\:'./  ' ( (
            (_(   .-'^^'-.   )_)
             ((  (o  \/  o) ))
              ))  \  ~~  / ((
                    '. .'
                      V
        """,
        # Vader helmet
        """
              .-.
            .-| |-.
           /  | |  \\
          |   |_|   |
          |  /   \  |
          | | o o | |
          |  \___/  |
          |_________|
        """,
        # R2-D2
        """
            .--.
           /    \\
          | •  • |
          |  __  |
          |______|
          |||||||| 
          ||||||||
        """
    ]
    print(random.choice(arts))

def hangman(secretWord):
    '''
    Main game function for Star Wars Hangman
    '''
    print("\n╔════════════════════════════════════════════════════════╗")
    print("║         Welcome to the Jedi Training Academy!          ║")
    print("║     Master Yoda has prepared a challenge for you.      ║")
    print("╚════════════════════════════════════════════════════════╝")
    
    showCharacterArt()
    
    print(f"\nYoda says: \"Sense a word I do... {len(secretWord)} letters it has.\"")
    print("Your lightsaber will lose power with each wrong guess!")
    print("8 mistakes, and to the Dark Side you will fall!\n")
    
    mistakesMade = 0
    lettersGuessed = []
    
    while mistakesMade < 8:
        
        if isWordGuessed(secretWord, lettersGuessed):
            print("\n" + "🌟"*30)
            print("         VICTORY! A JEDI YOU HAVE BECOME!")
            print(f"         The word was: {secretWord.upper()}")
            print("🌟"*30)
            print("\n" + getRandomQuote(YODA_QUOTES))
            print("\nMaster Yoda: \"Strong in the Force, you are!\"")
            break
            
        else:
            displayLightsaber(mistakesMade)
            print("═"*50)
            print(f"Force Energy: {'█' * (8-mistakesMade)}{'░' * mistakesMade} [{8-mistakesMade}/8]")
            print(f"Galactic Alphabet: {getAvailableLetters(lettersGuessed)}")
            print(f"Hidden Word: {getGuessedWord(secretWord, lettersGuessed)}")
            
            guess = str(input("\n⚔️  Choose your letter, young Padawan: ")).lower()
            
            if len(guess) != 1 or not guess.isalpha():
                print("❌ Invalid input! A single letter you must choose.")
                continue
                
            if guess in lettersGuessed:
                print(f"⚠️  Already tried that letter you have!")
                
            elif guess in secretWord:
                lettersGuessed.append(guess)
                print(f"✅ Well done! The Force is strong with you!")
                if random.random() > 0.7:  # 30% chance for a quote
                    print(f'"{getRandomQuote(OBI_WAN_QUOTES)}"')
                
            else:
                lettersGuessed.append(guess)
                mistakesMade += 1
                print(f"❌ Wrong! The Dark Side grows stronger...")
                if mistakesMade >= 4 and random.random() > 0.5:  # More Vader quotes as you fail
                    print(f'Vader: "{getRandomQuote(VADER_QUOTES)}"')
                
        if mistakesMade == 8:
            displayLightsaber(8)
            print("\n" + "💀"*30)
            print("         DEFEAT! THE EMPIRE HAS WON!")
            print(f"         The word was: {secretWord.upper()}")
            print("💀"*30)
            print("\nEmperor: \"Your feeble skills are no match for the Dark Side!\"")
            break

def playAgain():
    '''
    Ask if player wants to play again
    '''
    response = input("\nDo you wish to continue your training? (yes/no): ").lower()
    return response.startswith('y')

# Main game loop
if __name__ == "__main__":
    wordlist = loadWords()
    
    while True:
        secretWord = chooseWord(wordlist).lower()
        hangman(secretWord)
        
        if not playAgain():
            print("\nMay the Force be with you, always!")
            print("Farewell, young Jedi...\n")
            break