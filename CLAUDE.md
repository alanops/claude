# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a simple Python Hangman game implementation located in the `Hangman/Hangman Game/` directory. The project consists of a single Python script with no external dependencies.

## Commands

### Running the Game
```bash
cd "Hangman/Hangman Game"
python Hangman.py
```

## Architecture

The codebase is a single-file Python application:
- **Hangman.py**: Main game implementation with functions for word selection, game logic, and user interaction
- **words.txt**: Text file containing the word list for the game (one word per line)

Key functions in Hangman.py:
- `loadWords()`: Loads words from words.txt file
- `chooseWord(wordlist)`: Randomly selects a word from the loaded list
- `isWordGuessed(secretWord, lettersGuessed)`: Checks if the word has been completely guessed
- `getGuessedWord(secretWord, lettersGuessed)`: Returns the current state of the word with guessed letters revealed
- `getAvailableLetters(lettersGuessed)`: Shows remaining letters that haven't been guessed
- `hangman(secretWord)`: Main game loop handling user input and game state

## Known Issues

1. Bug at line 138 in Hangman.py: The lose condition message incorrectly shows "The word was else." instead of the actual word
2. The `isWordGuessed` function has incorrect logic - it counts character occurrences instead of checking if all unique letters in the word have been guessed