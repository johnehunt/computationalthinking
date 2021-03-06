# Loop over a set of values in a range
print('Print out values in a range')
for i in range(0, 10):
    print(i, ' ', end='')
print()
print('Done')

print('-' * 25)

# Now use values in a range but increment by 2
print('Print out values in a range with an increment of 2')
for i in range(0, 10, 2):
    print(i, ' ', end='')
print()
print('Done')

print('-' * 25)

# This illustrates the use of a break statement
num = int(input('Enter a number: '))
for i in range(0, 6):
    if i == num:
        break
    print(i, ' ', end='')
print('Done')

print('-' * 25)

# This illustrates the use of a continue statement
for i in range(0, 10):
    print(i, ' ', end='')
    if i % 2 == 1: # Determine if this is an odd number
        continue
    print('its an even number')
    print('we love even numbers')
print('Done')
