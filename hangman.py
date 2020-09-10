# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()
secret_word = choose_word(wordlist)

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    
    letters = list(secret_word)

    letters.sort()
    letters_guessed.sort()

    if letters == letters_guessed:
      return True
    else:
      return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    letters = list(secret_word)
    result = []

    if len(letters_guessed) == 0:
      result.append("_" * len(secret_word))

    for char in letters:
      if char not in letters_guessed:
        result.append("_")
      else: 
        result.append(char)
    res = ''.join(result)
    result.clear()
    return res
 

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabet = list(string.ascii_lowercase)

    for l1 in alphabet:
      for l2 in letters_guessed:
        if l1 == l2:
          alphabet.remove(l1)
    res = ''.join(alphabet)
    return res
  

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    word = list(my_word)

    if len(word) == len(other_word):
      for i in range(len(word)):
        if word[i] == other_word[i]:
          continue
        elif word[i] == "_" and other_word[i] not in word:
          continue
        else: 
          return False
      return True
    else:
      return False

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    result = []

    for other_word in wordlist:
      if match_with_gaps(my_word,other_word) == True:
        result.append(other_word)
    print("Possible matches: " + str(result))


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    letters_guessed = []
    secret = list(secret_word)
    length = len(secret_word)
    guesses = 6
    warnings = 3

    print("I am thinking of a word that is " + str(length) + " letters long")

    if warnings == 1:
      print("You have " + str(warnings) + " warning left.")
    else:
      print("You have " + str(warnings) + " warnings left.")

    while guesses > 0 and is_word_guessed(secret_word,letters_guessed) is False: 
      the_vowel = ["a","e","i","o","u"]
      print("----------------------")
      print("You have " + str(guesses) + " guesses left.")
      print("Availiable letters: " + get_available_letters(letters_guessed))
      guess = input("Please guess a letter: ")
      
      if guess == "*":
        my_word = get_guessed_word(secret_word, letters_guessed)
        show_possible_matches(my_word)

      elif guess.isalpha() == True and len(guess) == 1:
        guess.lower()
        if guess in letters_guessed:
          
            if warnings == 0:
              guesses -= 1
            else: 
              warnings -=1

            if warnings == 1: 
              print("Oops! You've already guessed that letter. You have 1 warning left:  " + get_guessed_word(secret_word, letters_guessed))
            else:
              print("Oops! You've already guessed that letter. You have " + str(warnings) + "warnings left:  " + get_guessed_word(secret_word, letters_guessed)) 

        elif guess in secret: 
          letters_guessed.append(guess) 
          print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
        
        else:
          if guess in the_vowel:
            guesses -= 2
            print("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed)) 
          else:
            guesses -= 1
            print("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed)) 

      else: 
        print("Oops! That is not a valid letter. You have " + str(warnings) + " warnings left: " + get_guessed_word(secret_word, letters_guessed))
        warnings -= 1
        if warnings == 0: 
          guesses -= 1 

    uniquness = len(set(secret)) * guesses 
    
    if is_word_guessed(secret_word,letters_guessed) is True:
      print("Congratulations, you won!")
      print("Your total score for this game is: " + str(uniquness)) 
    else: 
      print("Sorry, you ran out of guesses. The word was " + secret_word) 





if __name__ == "__main__":
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)


