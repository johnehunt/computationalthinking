# Provides numerous
# examples of different options for exception handling


def my_function(x, y):
    """
      A simple function to divide x by y
    """
    print('my_function in')
    solution = x / y
    print('my_function out')
    return solution


print('Starting')

print(my_function(6,  2))

try:
    print('Before my_function')
    result = my_function(6, 0)
    print(result)
    print('After my_function')
except:
    print('oops')

print('-' * 20)

try:
    print('Before my_function')
    result = my_function(6, 0)
    print(result)
    print('After my_function')
except ZeroDivisionError:
    print('oops')

print('-' * 20)

try:
    print('Before my_function')
    result = my_function(6, 0)
    print(result)
    print('After my_function')
except ZeroDivisionError as exp:
    print(exp)
    print('oops')

print('Done')

print('-' * 20)

try:
    print('Before my_function')
    result = my_function(6, 0)
    print(result)
    print('After my_function')
except ZeroDivisionError as exp:
    print(exp)
    print('oops')
else:
    print('All OK')

print('-' * 20)

try:
    result = my_function(6, 0)
    print(result)
except ZeroDivisionError as e:
    print(e)
else:
    print('Everything worked OK')
finally:
    print('Always runs')

print('-' * 20)

try:
    result = my_function(6, 0)
    print(result)
except Exception as e:
    print(e)

print('-' * 20)

try:
    print('Before my_function')
    result = my_function(6, 0)
    print(result)
    print('After my_function')
except ZeroDivisionError as exp:
    print(exp)
    print('oops')
except Exception as exp:
    print(exp)
    print('oh dear')
except:
    print('That is it')

print('-' * 20)

try:
    print('Before my_function')
    result = my_function(6, 0)
    print(result)
    print('After my_function')
finally:
    print('Always printed')