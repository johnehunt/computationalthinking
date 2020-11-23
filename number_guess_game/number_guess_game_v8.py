import random
from pathlib import Path

# Initialize the maximum number of guesses
MAX_NUMBER_OF_GUESSES = 5

# Print the Welcome Banner
print('===========================================')
print('          Welcome to the Number Guess Game')
print('      ', '-' * 40)
print("""
The Computer will ask you to guess a number between 1 and 10.
""")
print('===========================================')

current_low_score = 9999
# Check to see if the low score file is present
path_to_file = Path('low_score.txt')
if path_to_file.exists():
    with open('low_score.txt', 'r') as f:
        data = f.readline()
        if data.isdigit():
            current_low_score = int(data)

# Set up the game playing loop
game_over = False
while not game_over:

    # Initialise the number to be guessed
    number_to_guess = random.randint(1, 10)

    # Set up flag to indicate if one game is over
    finished_current_game = False

    # Initialise the number of tries the player has made
    count_number_of_tries = 0

    # Obtain their initial guess and loop to see if they guessed correctly
    while not finished_current_game:
        guess = None

        # Make sure input is a positive integer
        input_ok = False
        while not input_ok:
            input_string = input('Please guess a number between 1 and 10: ')

            # Adding a cheat mode
            if input_string == '-1':
                print('Cheat mode: number to guess is ', number_to_guess)
            elif input_string.isdigit():
                guess = int(input_string)
                count_number_of_tries += 1
                input_ok = True
            else:
                print('Input must be a positive integer')

        # Check to see if the guess is above, below or the correct number
        # Also Check to see they have not exceeded the maximum
        # number of attempts if so break out of loop otherwise
        # give the user come feedback
        if guess == number_to_guess:
            print('Well done you won!')

            # The player won - check to see if
            # we need to save the low score.
            if count_number_of_tries < current_low_score:
                print('----------', count_number_of_tries, current_low_score, count_number_of_tries < current_low_score)
                # Need to update the low score file
                current_low_score = count_number_of_tries
                with open('low_score.txt', 'w') as f:
                    f.write(str(current_low_score))

            # Now set the end of current game flag
            finished_current_game = True
        elif guess < number_to_guess:
            print('Your guess was lower than the number')
        elif guess > number_to_guess:
            print('Your guess was higher than the number')

        if not finished_current_game and count_number_of_tries == MAX_NUMBER_OF_GUESSES:
            print("Sorry - you loose, max number of guesses reached")
            print('The number you needed to guess was',
                  number_to_guess)
            finished_current_game = True

    # Check to see if the user wants to play another game
    response = input('Do you want to play again? (y/n): ')
    response = response.lower()  # convert input into lower case sot hat Y == y
    if response == 'n':
        game_over = True

print('Game Over')
