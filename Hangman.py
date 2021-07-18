import re
import random

incorrect_guesses = 0
correct_guesses = 0
guessed_list = []
new_hidden= ""
playing = True
word_list = list()

# Make list from .txt file
with open("wordlist.txt") as f:
    for line in f:
        word_list.append(line)
    
word_list = [line.rstrip('\n') for line in open("wordlist.txt")]

# Choose 1 word at random from list
def choose_word():
    return random.choice(wordList)


# Make the chosen word into a list of *'s
def make_hidden_list(chosen_word):
    hidden_list = []
    for letter in chosen_word:
        hidden_list.append("*")
    return hidden_list


# Make the chosen word into a string of *'s
def make_hidden_str(hidden_list):
    hidden_str = ""
    for i in hidden_list: 
        hidden_str += str(i) 
    return hidden_str


# Get an input from the user and return it as a variable called guess
def get_input():
    guess = input("Please enter your next guess: ")
    return guess


# Check that the input is valid. (Is 1 character long, is a letter, hasnt been used before)
def validate_input(guess):
    print("Your input was:", guess)
    if len(guess) > 1:
        print("Error! Only 1 characters allowed!")
        return False
    elif not re.match("^[a-z]*$", guess): 
        print("Error! Only lower case letters allowed!")
        return False
    elif guess in guessed_list:
        print("You have guessed this before.")
    elif guess == "":
        print("No input given.")
    else:
        return True
    

# Check if the guessed letter is in the word
def check_guess(guess):
    if guess in chosen_word_split:
        return True
    else:
        return False


# Change the output string/list to have the correctly guessed letter in it.
def correct_guess(is_correct):
    global correct_guesses
    if is_correct == True:
        print("Correct guess")
        for x in chosen_word_split:
            if x == guess:
                index_pos = chosen_word_split.index(guess)
                chosen_word_split[index_pos] = ""
                hidden_list[index_pos] = guess
                new_hidden = make_hidden_str(hidden_list)
                correct_guesses += 1
                print(new_hidden, "\n")


# Add 1 to incorrect_guesses variable.
def wrong_guess(is_correct):
    global incorrect_guesses, new_hidden
    if is_correct == False:
        print("Incorrect guess ")
        new_hidden = make_hidden_str(hidden_list)
        print(new_hidden, "\n")
        incorrect_guesses += 1



# Running the game
while True:
    
    #Start up code
    print('Welcome to Hangman! You have 7 chances to guess the hidden letters in an unknown word. You have no clues. Good luck!')
    #Making the list of words
    wordList = [line.rstrip('\n') for line in open("wordlist.txt")]
    #Choosing a word from list
    chosen_word = choose_word()
    chosen_word_split = list(chosen_word)
    # Making the chosen word into list and string foms of "*"
    hidden_list = make_hidden_list(chosen_word)
    hidden_str = make_hidden_str(hidden_list)
    print(hidden_str)
    
    while playing: 
        #Prompt for input
        while True:
            guess = get_input()
            #Validate input
            if validate_input(guess) == True:
                guessed_list.append(guess)
                break 
                
        #Check input against word
        is_correct = check_guess(guess)
        wrong_guess(is_correct)
        correct_guess(is_correct)

    # Checking if Won/Lost
        if incorrect_guesses >= 7: 
                    print("You lose!")
                    playing = False
                    print("The correct word was: ", chosen_word)
                    continue
        if correct_guesses >= len(chosen_word): 
                    print("You win!!")
                    playing = False
                    continue
    
    # Finishing game
    else:
        print("Thanks for playing!")
        break
