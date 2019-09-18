def runcalc(x):
    x / 0


def print_value(i, list):
    print(list[i])


def print_alt_value(i, list):
    if i > len(list):
        raise ValueError('Invalid length ' + str(i))
    print(list[i])


def my_function(x, y):
    print('my_function in')
    result = x / y
    print('my_function out')
    return result


def f2():
    print('f2 in')
    function_bang()
    print('f2 out')


def function_bang():
    print('function_bang in')
    raise ValueError('Bang!')
    print('function_bang out')


def divide(x, y):
    try:
        result = x / y
    except Exception as e:
        raise RuntimeError from e


divide(6, 0)

print('Starting')
try:
    print('Before my_function')
    my_function(6, 2)
    print('After my_function')
except ZeroDivisionError as exp:
    print('oops')
else:
    print('All OK')

print('Done')

try:
    my_function(6, 0)
except ZeroDivisionError as e:
    print(e)
else:
    print('Everything worked OK')
finally:
    print('Always runs')

try:
    function_bang()
except ValueError as ve:
    print(ve)
    raise

l = [1, 2, 3, 4]
try:
    print_alt_value(7, l)
except Exception as e:
    print(e)

l = [1, 2, 3, 4]
try:
    print_value(2, l)
    print_value(3, l)
except IndexError as e:
    print('Exception: ', e)
else:
    print('All OK')
finally:
    print('Always runs')

print(divide(3, 0))
