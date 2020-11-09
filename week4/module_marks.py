# Prompt for the the student's name
student_name = input('Please enter your name: ')

# Ask the user for the students marks
coursework_mark = int(input('Coursework mark: '))
exam_mark = int(input('Combined in-class test and exam: '))

# Check for a pass or fail
if coursework_mark < 35:
    print('Fail')
elif exam_mark < 35:
    print('Fail')
elif (coursework_mark + exam_mark) / 2 < 40:
    print('Fail')
else:
    print('You passed')