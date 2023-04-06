stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
 
import random

 
# Function to randomly select a word from dictionary
def get_word():
    # Path to the text file
    with open('words.txt', 'r') as f:
        # Reads each word after splitting
        words1 = f.read().splitlines()
    # Returns any random word   
    return random.choice(words1)
 
def hangman():
    # randomly chose a word form the list of words.
    chosen_word = get_word()
    # keep an empty list that is used to display the letters
    # and empty spaces in a word that user must guess.
    display = []
    for _ in chosen_word:
        display += "_"
 
    # the initial game variables setup.
    # Set the lives and variable that keeps track of loop that runs
    # the game
    end_of_loop = False
    lives = 6
 
    # display a welcoming message for the user.
    print("\n-------------Welcome to Hangman-------------\n")
    print("Guess the word:- ", end=" ")
    print(f"{' '.join(display)}")
    print(f"Lives: {lives}")
     
    while not end_of_loop:
        guess = input("Guess a Letter: ").lower()
        # reduce the lives if the guessed letter does not exist in the
        # word that user has to guess
        if not (guess in chosen_word):
            lives -= 1
        # now replace empty space of word with guessed letter if the
        # user guessed a letter that is in the word.
        index = 0
        for c in chosen_word:
            if c == guess:
                display[index] = guess
            index += 1
 
        # Again display the status of game.
        print(f"{' '.join(display)}")
        print(f"Lives: {lives}")
        print(stages[lives-1])
 
        # check of there are no _ in the display list, then that means
        # the user has guessed all the letters correctly.
        if "_" not in display:
            print("You Win")
            end_of_loop = True
 
        # check if he has run out of lives, then he has lost the game.
        if lives == 0:
            print("You Lose")
            print(f"The word was: {chosen_word}")
            end_of_loop = True
 
# The loop that will keep calling the game play function again and again unless the user does not want to play it anymore.
end_of_game = False
while not end_of_game:
    # ask user if he wants to play the game
    ask = input("Do you want to play Hangman? (y/n): ").lower()
    # if he insert yes, then call the function for playing the game.
    if ask == 'y' or ask == 'yes':
        hangman()
    # if the answer is no, quit the loop and end the program.
    elif ask == 'n' or ask == 'no':
        print("Program Exit Successful")
        end_of_game = True
    # if the user entered something else, ask again.
    else:
        print("Your given input could not be processed.")
        print("Please enter a correct input.")