# An implementation of the incorrect algorithm

component_a_mark = int(input('Please enter your mark for Component A: '))
coursework_mark = int(input('Please enter your mark for Component B: '))

module_mark = int(input('Please enter your mark for the module: '))

print('Calculating your result')

if module_mark >= 40:
    print('You have passed the module')

if coursework_mark < 35:
    print('You have not passed the module')

if component_a_mark < 35:
    print('You have not passed the module')
