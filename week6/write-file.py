print('Writing file')
f = open('my-new-file.txt', 'w')

# \n means newline
f.write('Hello from Python!!' + '\n')
f.write('Working with files is easy...\n')
f.write('It is cool ...\n')

f.write(str(42))  # Note write takes a string
f.write('\n')
f.close()
