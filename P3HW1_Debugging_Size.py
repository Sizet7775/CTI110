# CTI-110
# P3HW1 - Debugging
#Thomas Size
#October 24, 2022


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = (mod_1, mod_2, mod_3, mod_4, mod_5, mod_6)
# TO DO: determine lowest, highest , sum and average for grades

low_grade = min(grades)
high_grade = max(grades)
total_grade = sum(grades)
avg_grade = (sum(grades) / len(grades))

print('\n------------Results------------')
print(f'Lowest Grade: {low_grade: >10}')
print(f'Highest Grade: {high_grade: >9}')
print(f'Sum of Grades: {total_grade: >10}')
print(f'Average: {avg_grade: >16.2f}')
print('-------------------------------')

# determine letter grade for average


if avg_grade >= 90:
    print('Your grade is: A')
elif 89 > avg_grade >= 80:
    print('Your grade is: B')
elif 79 > avg_grade >= 70:
    print('Your grade is: C')
elif 69 > avg_grade >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F') # TO DO: finish this





