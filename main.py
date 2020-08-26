from random import choice
from interface import interface
from interface import summary
import string

incorrectGuesses = []       # To show what incorrect letters that you've already guessed
attempts = 0                # Number of attempts

# Create a list for the actual word and the the blank version of the words
alphabet = list(string.ascii_lowercase)

hangmans = interface()                                  # Allows printing of hangman 
words = ['library','stitch','chemical','amuck', 'crooked', 'filthy', 'humor', 'cut', 'slimy', 'coil', 'basket', 'adhesive']                # Random list of words
randomword = list(choice(words))

word = randomword

guessedword = []


for letter in range(len(word)):  # For each letter in the range amount of letters
  
    if word[letter] in alphabet: # if the word is an alphabet, dash ("-")

      guessedword.append('-')
    
    elif word[letter] == ' ':    # if the word is an alphabet, space

      guessedword.append(' ')


while attempts != 7 or guessedword != (''.join(word)):

    error = ''    

    # Prints hangman interface, then incorrectGuesses guesses made then the blank word
    
    summary(hangmans, attempts, incorrectGuesses, guessedword)

    guess = ''    

    # While you input anything but a letter, the same the letter previously found or more than 1 letter

    while guess.isdigit() or not guess.isalpha() or len(guess) > 1 or guess in guessedword or guess in incorrectGuesses:
      
      print(error)
      guess = input('Guess a letter: ')      # Asks for input
      
      if len(guess) > 1:                   # Input more than 1 letter e.g. "ad"

        error = '\nPlease enter 1 letter\n'
        summary(hangmans, attempts, incorrectGuesses, guessedword)

      elif guess.isdigit() or not guess.isalpha():   # Input anything but letter

        error = '\nPlease enter a letter\n'
        summary(hangmans, attempts, incorrectGuesses, guessedword)
        
      elif guess in guessedword or guess in incorrectGuesses:                     # Input already found letter

        error = '\nYou already guessed that letter\n'
        summary(hangmans, attempts, incorrectGuesses, guessedword) 
      
      elif guess not in word:                          # if you didn't input the right letter

        if guess not in incorrectGuesses:
          
          error = '\nWrong letter\n'
          attempts += 1
          incorrectGuesses.append(guess)
          summary(hangmans, attempts, incorrectGuesses, guessedword) 
      
    for letter in range(len(word)):             # For x each letter in the range amount of letters...

      if guess == word[letter]:                  # Replace the blank spots with each correct letter that you guessed  
        guessedword[letter] = guess
    
    if attempts == 7:

      summary(hangmans, attempts, incorrectGuesses, guessedword)
      msg = '\nGame Over'
      break

    elif guessedword == word:                      # if the guessed word matches the actual word, stop 

      msg = '\nYou Won!'
      summary(hangmans, attempts, incorrectGuesses, guessedword)
      break
      
    
print(msg)
print(f"\nThe word is: {(''.join(word))}")

  