# Simple reverse polish notation calculator

PROMPT = 'Please enter expression: '


def tokenize(string):
    """ Split the input into the constituent elements
        that comprise it for example convert the string  '2 3 +'
        into a list [2, 3, '+'] """
    tokens = string.split(' ')
    # Create a list to hold the results to return
    # A list is a bit like a growable array of things
    results = []

    # Loop through each of the elements in the tokens. If the 'token'
    # is actually an integer convert it to an int and add it to the results
    # otherwise just add it
    for token in tokens:
        if token.isdigit():
            results.append(int(token))
        else:
            results.append(token)

    return results


def print_message(message):
    """ Provide for a standardized prompt """
    print('->', message)


# Print a welcome message
print('Enter an expression at the prompt using Reverse Polish Notation (or q to quit)')
print('Note only integers are supported')

input_str = input(PROMPT)
# Check to see if the user wants to quit
while input_str != 'q':
    # Convert the input string into tokens
    input_tokens = tokenize(input_str)

    try:

        # Obtain the two operands and the operator
        # You can use an index to access elements from a list
        # note that the list is indexed from zero
        operand_1 = input_tokens[0]
        operand_2 = input_tokens[1]

        operator = input_tokens[2]

        # Test to see which operator has been provided
        if operator == '+':
            print_message(operand_1 + operand_2)
        elif operator == '-':
            print_message(operand_1 - operand_2)
        elif operator == '*':
            print_message(operand_1 * operand_2)
        elif operator == '/':
            print_message(operand_1 / operand_2)
        elif operator == '//':
            print_message(operand_1 // operand_2)
        elif operator == '%':
            print_message(operand_1 % operand_2)
        else:
            print_message('Invalid operator - try again!')

    except ZeroDivisionError:
        # Check for divide by Zero errors
        print_message('Cannot Divide By Zero - try again!')
    except TypeError:
        # Handle situation where operands ar enot integers
        print_message('The Operands must be Integers but you entered: ' + str(input_tokens))

    # Get the next input form the user
    input_str = input(PROMPT)

print('Done')
