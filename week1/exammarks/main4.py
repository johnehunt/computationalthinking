# Alternative solution using compound conditional statement

in_class_test = int(input('Please enter your mark for the In Class Test: '))
exam_mark = int(input('Please input your mark for the exam: '))
coursework_mark = int(input('Please enter your mark for Component B: '))

# Calculating mark by adding the marks together and dividing by 2
component_a_mark = (in_class_test * 0.25) + (exam_mark * 0.75)
module_mark = (component_a_mark + coursework_mark) / 2

print('Your mark is', module_mark, 'Calculating your result')

# Uses compound boolean proposition
if coursework_mark < 35 and component_a_mark < 35:
    print('You have not passed the module')
elif module_mark < 40:
    print('You have failed the module')
else:
    print('You have passed the module')