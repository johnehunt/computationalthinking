import random

# Initialize the maximum number of guess
MAX_NUMBER_OF_GUESSES = 4

# Print the Welcome Banner
print("=" * 60)
print('          Welcome to the Number Guess Game')
print('      ', '-' * 40)
print("""
The Computer will ask you to guess a number between 1 and 10.
You will have', MAX_NUMBER_OF_GUESSES, 'attempts to guess the 
correct number.
""")
print("=" * 60)

# Set up the game playing loop
game_over = False
while not game_over:

    # Initialise the number to be guessed
    number_to_guess = random.randint(1, 10)

    # Initialise the number of tries the player has made
    count_number_of_tries = 0

    # Set up flag to indicate if one game is over
    finished_current_game = False

    # Obtain their initial guess and loop to see if they guessed correctly
    while not finished_current_game:
        guess = int(input('Please guess a number between 1 and 10: '))
        count_number_of_tries += 1

        # Check to see they have not exceeded the maximum
        # number of attempts if so break out of loop otherwise
        # give the user come feedback
        if count_number_of_tries == MAX_NUMBER_OF_GUESSES:
            print("Sorry - you loose")
            print('The number you needed to guess was',
                  number_to_guess)
            finished_current_game = True
        elif guess < number_to_guess:
            print('Your guess was lower than the number')
        elif guess > number_to_guess:
            print('Your guess was higher than the number')
        else:
            print('Well done you won!')
            print('You took', count_number_of_tries, 'goes to complete the game')
            finished_current_game = True

    # Check to see if the user wants to play another game
    response = input('Do you want to play again? (y/n): ')
    response = response.lower()
    if response == 'n':
        game_over = True

print('Game Over')
