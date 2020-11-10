# One possible solution to the corrected algorithm

component_a_mark = int(input('Please enter your mark for Component A: '))
coursework_mark = int(input('Please enter your mark for Component B: '))

print('Calculating your result')

# Calculating mark by adding the marks together and dividing by 2
module_mark = (component_a_mark + coursework_mark) / 2
print('Your module mark is', module_mark)

if coursework_mark < 35 or component_a_mark < 35:
    print('You have not passed the module')
elif module_mark < 40:
    print('You have failed the module')
else:
    print('You have passed the module')

