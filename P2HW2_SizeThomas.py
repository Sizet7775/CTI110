# CTI-110
# P2HW2 - List
# Thomas Size
# October 14, 2022

#Create a list
#Add user input to list for each module grade
#Format average to 2 decimals
#Display lowest grade
#Display highest grade
#Display sum of grades
#Display average of grades formatted to 2 decimals
mod_grades_list = []
mod_grades_list.append (float(input('Enter grade for Module 1: ')))
mod_grades_list.append (float(input('Enter grade for Module 2: ')))
mod_grades_list.append (float(input('Enter grade for Module 3: ')))
mod_grades_list.append (float(input('Enter grade for Module 4: ')))
mod_grades_list.append (float(input('Enter grade for Module 5: ')))
mod_grades_list.append (float(input('Enter grade for Module 6: ')))
mod_grades_avg = (f'{(sum(mod_grades_list)) / (len(mod_grades_list)): .2f}')

print ('\n------------Results------------')
print (f'Lowest Grade: {min(mod_grades_list): >9}')
print (f'Highest Grade: {max(mod_grades_list): > 9}')
print (f'Sum of Grades: {sum(mod_grades_list): >9}')
print (f'Average: {mod_grades_avg: >15}')
print ('-------------------------------')
