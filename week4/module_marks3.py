# Version that checks for valid input

# Prompt for the the student's name
student_name = input('Please enter your name: ')

# Ask the user for the students marks
# Initially input as a string
coursework_mark = input('Coursework mark: ')
if coursework_mark.isdigit():
    coursework_mark = int(coursework_mark)
else:
    print('Your course mark should be a positive integer')
    coursework_mark = -1

exam_mark = input('Combined in-class test and exam: ')
if exam_mark.isdigit():
    exam_mark = int(exam_mark)
else:
    print('Your combined in-class test and exam should be a positive integer')
    exam_mark = -1

# Check for a pass or fail
if coursework_mark == -1 or exam_mark == -1:
    print('Invalid input')
elif coursework_mark < 35:
    print('Fail')
elif exam_mark < 35:
    print('Fail')
elif (coursework_mark + exam_mark) / 2 < 40:
    print('Fail')
else:
    print('You passed')