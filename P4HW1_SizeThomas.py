# CTI-110
# P4HW1 - List with loops
# Thomas Size
# November 7, 2022

#Create a list
#Add user input to list for each module grade
#Exclude input outside the range of 0-100
#Format average to 2 decimals
#Display lowest grade
#Drop lowest score and display new list
#Average the scores of the new list
#Display letter grade based on average score

mod_grades_list = []
mod_grade_1 = (float(input('Enter grade for Module 1: ')))
while mod_grade_1 < 0 or mod_grade_1 > 100:
    print('INVALID Score entered!!!!')
    print('Score should be between 0 and 100')
    mod_grade_1 = (float(input('Enter score #1 again: ')))
else:
    mod_grades_list.append (mod_grade_1)
mod_grade_2 = (float(input('Enter grade for Module 2: ')))
while mod_grade_2 < 0 or mod_grade_2 > 100:
    print('INVALID Score entered!!!!')
    print('Score should be between 0 and 100')
    mod_grade_2 = (float(input('Enter score #2 again: ')))
else:
    mod_grades_list.append (mod_grade_2)
mod_grade_3 = (float(input('Enter grade for Module 3: ')))
while mod_grade_3 < 0 or mod_grade_3 > 100:
    print('INVALID Score entered!!!!')
    print('Score should be between 0 and 100')
    mod_grade_3 = (float(input('Enter score #3 again: ')))
else:
    mod_grades_list.append (mod_grade_3)
mod_grade_4 = (float(input('Enter grade for Module 4: ')))
while mod_grade_4 < 0 or mod_grade_4 > 100:
    print('INVALID Score entered!!!!')
    print('Score should be between 0 and 100')
    mod_grade_4 = (float(input('Enter score #4 again: ')))
else:
    mod_grades_list.append (mod_grade_4)
mod_grade_5 = (float(input('Enter grade for Module 5: ')))
while mod_grade_5 < 0 or mod_grade_5 > 100:
    print('INVALID Score entered!!!!')
    print('Score should be between 0 and 100')
    mod_grade_5 = (float(input('Enter score #5 again: ')))
else:
    mod_grades_list.append (mod_grade_5)
mod_grade_6 = (float(input('Enter grade for Module 6: ')))
while mod_grade_6 < 0 or mod_grade_6 > 100:
    print('INVALID Score entered!!!!')
    print('Score should be between 0 and 100')
    mod_grade_6 = (float(input('Enter score #6 again: ')))
else:
    mod_grades_list.append (mod_grade_6)


print ('\n------------Results------------')
print (f'Lowest Grade  : {min(mod_grades_list)}')

mod_grades_list.remove(min(mod_grades_list))
mod_grades_avg = (sum(mod_grades_list)) / (len(mod_grades_list))
mod_grades_avg_form = (f'{(sum(mod_grades_list)) / (len(mod_grades_list)): .2f}')

print (f'Modified List : {mod_grades_list}')
print (f'Scores Average:{mod_grades_avg_form}')
if mod_grades_avg >= 90:
    print(f'Grade         : A')
elif 89 > mod_grades_avg >= 80:
    print(f'Grade         : B')
elif 79 > mod_grades_avg >= 70:
    print(f'Grade         : C')
elif 69 > mod_grades_avg >= 60:
    print(f'Grade         : D')
else:
    print(f'Grade         : F')
print ('-------------------------------')
