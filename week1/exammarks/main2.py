# Alternative solution using componed conditional statement

component_a_mark = int(input('Please enter your mark for Component A: '))
coursework_mark = int(input('Please enter your mark for Component B: '))

module_mark = int(input('Please enter your mark for the module: '))

print('Calculating your result')

# Uses compound boolean proposition
if coursework_mark < 35 and component_a_mark < 35:
    print('You have not passed the module')
elif module_mark < 40:
    print('You have failed the module')
else:
    print('You have passed the module')