#CTI-110
#P3HW2 - Salary
#Thomas Size
#October 24, 2022

#Get employee name
#Get hours worked
#Get pay rate
#Display employee name
#Display hours worked
#Display pay rate
#Display overtime as hours worked over 40
#Display total amount of overtime pay as 1.5 x pay rate per hour
#Dsplay and format total amount of regular pay
#Display and format gross pay as regular pay + overtime pay

employee_name = input('Enter employee\'s name: ')
hours_worked = float(input('Enter number of hours worked: '))
pay_rate = float(input('Enter emplyee\'s pay rate: '))
overtime = (hours_worked % 40)
overtime_pay = overtime * (pay_rate * 1.5)
reghour_pay = hours_worked * pay_rate
gross_pay = reghour_pay + overtime_pay
reghour_pay_dollars = '${:.2f}'.format(reghour_pay)
gross_pay_dollars = '${:.2f}'.format(gross_pay)

print('-------------------------------')
print('Empolyee name: ') , employee_name
print('Hours Worked    Pay Rate    OverTime    Overtime Pay        RegHour Pay        Gross Pay')
print('------------------------------------------------------------------------------------------')
print(f'{hours_worked} {pay_rate: >15} {overtime: >10} {overtime_pay: >14} {reghour_pay_dollars: >20} {gross_pay_dollars: >18}')
