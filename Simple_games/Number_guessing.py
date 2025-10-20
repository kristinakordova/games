## Guessing game
from random import randint
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def get_lives():
    """Function to get number of lives based on difficulty"""
    difficulty = input(str("Choose difficulty. Type 'easy' or 'hard':"))
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    elif difficulty == "hard":
        return HARD_LEVEL_TURNS
    else: ValueError("Not recognised responce. You can only use 'easy' or 'hard'")

def check_guess(guess_number, chosen_number, lives_left):
    """Functions checks the number the user guessed versus the correct number.
    Returns the number of lies remaining"""
    if guess_number == chosen_number:
        print("You guessed correctly!")
    if guess_number > chosen_number:
        print("Too high")
        return lives_left - 1
    if guess_number < chosen_number:
        print("Too low")
        return lives_left - 1
    
def game ():
    #first a random numebr is chosen
    print("I am thinking of a number between 1 and 100")
    chosen_number = randint(1,100)


    #choose difficulty to determine number of lives
    lives_left = get_lives()
    print(f"Number of lives {lives_left}")

    guess_number = 0
    while guess_number!=chosen_number:
        print(f"Lives left: {lives_left}")
        guess_number = int(input("Guess a number "))
        lives_left = check_guess(guess_number, chosen_number, lives_left)
        if lives_left == 0:
            print("You ran out of lives.")
            return 

    print(f"Chosen number was {chosen_number}")

game()