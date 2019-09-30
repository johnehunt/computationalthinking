# Examples of using logical operators such as And, Or and Not

print('Logical operators')
print('-' * 20)
# Change the following variable between True and False and
# see what the result is
flag1 = True
flag2 = True

print('flag1 and flag2: ', flag1 and flag2)
print('flag1 or flag2: ', flag1 or flag2)
print('not flag1: ', not flag1)

print()
print('Numerical Comparison operators')
print('-' * 30)
# Change the value of 10 and see the result
i = 6
j = 5

print('i == j:', i == j)
print('i != j:', i != j)
print('i > j:', i > j)
print('i < j:', i < j)
print('i <= j:', i <= j)
print('i >= j:', i >= j)

print()
print('Logical and numerical operators')
print('-' * 30)
# Change the value of 10 and see the result
x = 10
y = 6

print('x < 10 and y > 5:', x < 10 and y > 5)
print('x < 10 or y > 5:', x < 10 or y > 5)
print('not(x < 10 and y > 5):', not(x < 10 and y > 5))