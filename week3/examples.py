# x = 0
# y = 0
# z = 0

# Assignment
x = y = z = 0
print(x)

# Be careful of this
print(2 + 2 * 2 - 1 // 2)
# print(2 + 2 * 2 - 1)

# Strings can be
string1 = 'John'
string2 = "John"
string3 = """John"""

# Substrings
my_string = 'John was here'
print(my_string[3])
print(my_string[3:])
print(my_string[3:6])
print(my_string[:6])

cont = input('Do you want to continue (y/n)?')
cont = cont.lower()
if cont == 'n':
    print('Game over')

age = input('please enter age: ')

if age.isnumeric():
    age = int(age)
    print('yeah')
    if age < 18:
        print('You are under 18')
else:
    print('Its not an integer')

print(age)
