# File type implements the Context Manager Protocol
# can therefore use a file in a 'with as' statement

with open('myfile2.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')
print()

