file = open('myfile.txt', 'r')

# Returns the contents of the file as a list of strings
lines = file.readlines()
for line in lines:
    print(line, end='')

# Remember to always close the file
file.close()
