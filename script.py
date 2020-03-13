'''
Created by: Ramy Ibrahim
Date: 12 March 2020
Supervised by: Dr. Younes Gamal Elddin
'''

def calculate_grade(mark):
    grade = ''
    if mark >= 81:
        grade = 'Excellent'
    elif mark >= 71:
        grade = 'Very Good'
    elif mark >= 61:
        grade = 'Good'
    elif mark >= 51:
        grade = 'Weak'
    elif mark == 50:
        grade = 'Pass'
    else:
        grade = 'Fail'
    return grade

###

student_name = 'Ramy Ibrahim'
student_id = '20201000071'

print('Name:', student_name)
print('ID:', student_id)

print('\nGrades:')
print('Python Programming 101:', calculate_grade(87))
print('Math:', calculate_grade(81))
print('Physics:', calculate_grade(71))
print('English:', calculate_grade(50))