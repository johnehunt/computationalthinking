import random

# Print the Welcome Banner
print('===========================================')
print('          Welcome to the Number Guess Game')
print('      ', '-' * 40)
print("""
The Computer will ask you to guess a number between 1 and 10.
""")
print('===========================================')

# Initialise the number to be guessed
number_to_guess = random.randint(1, 10)

# Set up flag to indicate if one game is over
finished_current_game = False

# Obtain their initial guess and loop to see if they guessed correctly
while not finished_current_game:
    guess = None

    # Make sure input is a positive integer
    input_ok = False
    while not input_ok:
        input_string = input('Please guess a number between 1 and 10: ')
        if input_string.isdigit():
            guess = int(input_string)
            input_ok = True
        else:
            print('Input must be a positive integer')

    # Check to see if the guess is above, below or the correct number
    if guess < number_to_guess:
        print('Your guess was lower than the number')
    elif guess > number_to_guess:
        print('Your guess was higher than the number')
    else:
        print('Well done you won!')
        finished_current_game = True

print('Game Over')
