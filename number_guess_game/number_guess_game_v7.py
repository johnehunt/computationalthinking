# Illustrates using a list to maintain a history of
# guesses in the number guess game

import random

# Initialise the number to be guessed
NUMBER_TO_GUESS = random.randint(1, 10)

# List to hold guesses
guess_history = []


def welcome_message():
    print('Welcome to the number guess game')


def game_over_message():
    print('Game Over')


def get_user_input(prompt):
    invalid_input = True
    while invalid_input:
        print(prompt)
        user_input = input()
        if not user_input.isdigit():
            print('Input must be a number')
        else:
            user_input_int = int(user_input)
            if (user_input_int < 1 or user_input_int > 10):
                print('input must be a number in the range 1 to 10')
            else:
                invalid_input = False
    return user_input_int


def play_game():
    """ Defines main loop controlling game"""
    # Initialise the number of tries the player has made
    count_number_of_tries = 1

    # Obtain their initial guess
    guess = get_user_input('Please guess a number between 1 and 10: ')
    while NUMBER_TO_GUESS != guess:
        print('Sorry wrong number')

        # Add guess to guess history
        guess_history.append(guess)

        # Check to see they have not exceeded the maximum
        # number of attempts if so break out of loop otherwise
        # give the user come feedback
        if count_number_of_tries == 4:
            break
        elif guess < NUMBER_TO_GUESS:
            print('Your guess was lower than the number')
        else:
            print('Your guess was higher than the number')

        # Obtain their next guess and increment number of attempts
        guess = int(input('Please guess again: '))
        count_number_of_tries += 1

    guess_history.append(guess)
    return guess


def check_for_a_win(guess):
    """ Check to see if they did guess the correct number """
    if NUMBER_TO_GUESS == guess:
        print('Well done you won!')
    else:
        print("Sorry - you loose")
        print('The number you needed to guess was',
              NUMBER_TO_GUESS)


welcome_message()

last_guess = play_game()
check_for_a_win(last_guess)

print('The guesses you made were:')
for guess in guess_history:
    print('Guess: ', guess)

game_over_message()
