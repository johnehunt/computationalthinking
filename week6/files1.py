# Open the file
file = open('myfile.txt', 'r')

# Access some properties of the file
print('file.name:', file.name)
print('file.closed:', file.closed)
print('file.mode:', file.mode)

# Close the link to the file
file.close()
print('file.closed now:', file.closed)
