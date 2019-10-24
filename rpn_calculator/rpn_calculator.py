# Slightly more sophisticated Reverse Polish Notation calculator

PROMPT = 'Please enter expression: '
VALID_OPERATORS = '+ * - / // %'


def is_float(text):
    print(text.isalpha())
    print('.' in text)
    """ Takes a string and returns true if it is a floating point number """
    if text.isnumeric():
        return False
    else:
        try:
            float(text)
            return True
        except:
            return False


def is_integer(text):
    """ Tests to see if a string contains an integer """
    if text.isdigit():
        return True
    elif text[0] == '-':  # Check for negative numbers
        if text[1:].isdigit():
            return True
    else:
        return False


def is_operator(text):
    return text in VALID_OPERATORS


def return_number_or_string(text):
    """ Check to see if a string contains an int or a float and return as appropriate """
    if is_operator(text):
        return text
    elif text.isalpha():
        return text
    elif is_integer(text):
        return int(text)
    elif is_float(text):
        return float(text)
    else:
        return text


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
    """ Generate a standard output message format"""
    print('->', message)


def perform_calculation(operand1, operand2, operator):
    """ Given two operands (numbers) perform the associated operation """
    if isinstance(operand1, str) or isinstance(operand2, str):
        raise TypeError('Operands must be a number')
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2
    elif operator == '//':
        return operand1 // operand2
    elif operator == '%':
        return operand1 % operand2
    else:
        raise RuntimeError('Invalid Operation, must be one of', VALID_OPERATORS)


def print_welcome_banner():
    """ Print the banner heading """
    print()
    print(' ' * 10, "Welcome to the 'RPN' Calculator")
    print(' ' * 8, '=' * 35)
    print()
    print('-' * 90)
    print("""
    Enter an expression at the prompt using Reverse Polish Notation (or q to quit)'
    
    Reverse Polish notation (RPN) is a mathematical notation in which operators follow their 
    operands.
    
    It does not need any parentheses as long as each operator has a fixed number of operands.
    For example, to add 3 and 4, you would write 3 4 + rather than 3 + 4.
    
    If there are multiple operations, operators are given immediately after their second operands; 
    therefore the expression written 3 − 4 + 5 in conventional notation would be written 
    3 4 − 5 + in Reverse Polish Notation.
    """)
    print('-' * 90)
    print()


def main():
    print_welcome_banner()

    # Start the processing loop
    input_str = input(PROMPT)
    while input_str != 'q':

        # Convert the input string into a set of tokens to process
        input_tokens = tokenize(input_str)
        # print(input_tokens)

        try:

            # Set the initial value for the accumulator
            accumulator = input_tokens[0]

            # Now loop through remaining values and operators
            # Each remaining sequence should be a value followed by an operator
            index = 1
            while index + 1 < len(input_tokens):
                # Retrieve the value and the operator
                operand = input_tokens[index]
                operator = input_tokens[index + 1]

                # Perform the specified calculation using the accumulator and the value
                accumulator = perform_calculation(accumulator, operand, operator)

                # Move the index forward two to reference the next value and operator
                # If they exist
                index = index + 2

            # Print out the result which is held in the accumulator
            print_message(accumulator)

        except ZeroDivisionError:
            # Deal with any divide by zero errors
            print_message('Cannot Divide By Zero - try again!')
        except TypeError:
            # Deal with any errors where a user has not entered an appropriate value
            print_message('The Operands must be numbers but you entered: ' + str(input_tokens))
        except RuntimeError:
            # Handle the situation where the user has not entered an appropriate operator
            print_message('Operators must be one of [+, -, *, /, //, %]')

        input_str = input(PROMPT)

    print('\nDone')


if __name__ == '__main__':
    main()
