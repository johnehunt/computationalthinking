# Program to calculate tax band
print('Start')

# Set up 'constants' to be used
BASIC_RATE_THRESHOLD = 12500
HIGHER_RATE_THRESHOLD = 50000
ADDITIONAL_RATE_THRESHOLD = 150000

# Get user input and a number
income_string = input('Please input your income: ')
if income_string.isnumeric():
    annual_income = int(income_string)
    # Determine tax band
    if annual_income > ADDITIONAL_RATE_THRESHOLD:
        print('Calculating tax ...')
        print('Your highest tax rate is 45%')
    elif annual_income > HIGHER_RATE_THRESHOLD:
        print('Your highest tax rate is 40%')
    elif annual_income > BASIC_RATE_THRESHOLD:
        print('Your highest tax rate is 20%')
    else:
        print('You are not liable for income tax')
else:
    print('Input must be a positive integer')

print('Done')
