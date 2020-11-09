# Prompt for the the student's name
student_name = input('Please enter your name: ')

# Ask the user for the students marks
coursework_mark = int(input('Coursework mark: '))
first_exam_mark = int(input('first exam mark: '))
second_exam_mark = int(input('second exam mark: '))

coursework_mark = coursework_mark * 0.6
first_exam_mark = first_exam_mark * 0.15
second_exam_mark = second_exam_mark * 0.25

module_mark = coursework_mark + first_exam_mark + second_exam_mark

print("\nDear", student_name)
print("Your total mark for this module is", str(int(module_mark))+'%')
