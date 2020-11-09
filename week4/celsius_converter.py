print('Starting')

celsius_string = input('Please enter a value in celsius: ')
celsius = int(celsius_string)

print('You entered', celsius)

# Fahrenheit = Celsius x 9 / 5 + 32
fahrenheit = celsius * 9
fahrenheit = fahrenheit / 5
fahrenheit = fahrenheit + 32

# or you coudl write
# fahrenheit = ((celsius * 9) / 5) + 32

print('Fahrenheit:', fahrenheit)

print('Done')