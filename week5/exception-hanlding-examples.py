# The exmaples in this file all illustrate hoe exception handling works

# The following code throws a TypeError - uncomment it to see
# name = 'John'
# age = 21
# print('Hello ' + name + ' you are ' + age)


# The following function will throw a ZeroDivisionError if the second
# value passed to it is zero


def runcalc(value1, value2):
    if value2 == 0:
        raise ZeroDivisionError('Division by Zero')
    return value1 / value2


print('-' * 25)

# This illustrates handling the ZeroDivisionError
try:
    runcalc(6, 0)
except ZeroDivisionError as exp:
    print(exp)
    print('opps')

print('-' * 25)
print('Try again')

# This illustrates being able to handle a series of
# different exceptions or errors
try:
    runcalc(6, 0)
except ZeroDivisionError:
    print('oops')
except IndexError:
    print('arrgh')
except FileNotFoundError:
    print('huh!')
except Exception:
    print('Duh!')
