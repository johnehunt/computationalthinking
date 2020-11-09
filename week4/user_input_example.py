# Illustrates using a while loop to process input
# as a number and verify that it is in a valid range

MIN_VALUE = 1
MAX_VALUE = 100
PROMPT = 'Please enter a number between ' + str(MIN_VALUE) + ' and ' + str(MAX_VALUE) + ': '

input_processing_complete = False

while not input_processing_complete:
    input_string = input(PROMPT)
    if input_string.isdigit():
        # The user entered a number
        print('Processing input')
        value = int(input_string)
        # Now check that the input is in the valid range
        if MIN_VALUE <= value <= MAX_VALUE:
            print('Input in valid range')
            input_processing_complete = True
        else:
            print('Input outside acceptable range')
    else:
        print('The input was not a valid positive number')
