# Alternative solution using compound conditional statement

component_a_mark = int(input('Please enter your mark for Component A: '))
coursework_mark = int(input('Please enter your mark for Component B: '))

# Calculating mark by adding the marks together and dividing by 2
module_mark = (component_a_mark + coursework_mark) / 2

print('Your mark is', module_mark, 'Calculating your result')

# Uses compound boolean proposition
if coursework_mark < 35 and component_a_mark < 35:
    print('You have not passed the module')
elif module_mark < 40:
    print('You have failed the module')
else:
    print('You have passed the module')