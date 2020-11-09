print('Starting')

# Obtain user details
first_name = input('Please enter your first name: ')
surname_name = input('Please enter your second name: ')
degree_name = input('Please enter your degree name: ')

print(first_name, surname_name, 'you are studying', degree_name)

# Obtain elements for module mark
coursework_mark_string = input('Please input the course mark: ')
coursework_mark = int(coursework_mark_string)

firstexam_mark_string = input('Please input the first exam mark: ')
firstexam_mark = int(firstexam_mark_string)

secondexam_mark = int(input('please enter your second exam mark: '))

# Output mark data
print('Coursework mark is' , coursework_mark)
print('First exam mark is' , firstexam_mark)
print('Second exam mark is' , secondexam_mark)

# Calculate the module mark
# calculate module mark = 
#      60% coursework mark + 
#      15% first exam mark + 
#      25% second exam mark

coursework_percentage = coursework_mark * 0.6
firstexam_percentage = firstexam_mark * 0.15
secondexam_percentage = secondexam_mark * 0.25

print('course work percentage: ', coursework_percentage)
print('first exam percentage: ', firstexam_percentage)
print('second exam percentage: ', secondexam_percentage)

module_mark = coursework_percentage + firstexam_percentage + secondexam_percentage

print(first_name, surname_name, 'you got', module_mark)

print('Done')