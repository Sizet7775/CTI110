#Travel expense calculator
#September 19, 2022
#CTI-110 P1HW2 - Travel Expense
#Thomas Size
#
print ('This program calculates and displays travel expenses')
budget_amount = int(input('Enter Budget: '))
destination = input('Enter destination: ')
gas_budget = int(input('How much will you spend on gas? '))
hotel_budget = int(input('How much will you spend on lodging? '))
food_budget = int(input('How much will you spend on food? '))
print()
print ('------------Travel Expenses------------')
print ('Location: ' , destination)
print ('Initial budget: ' , budget_amount)
print ()
print ('Fuel: ' , gas_budget)
print ('Accomodation: ' , hotel_budget)
print ('Food: ' , food_budget)
print ()
print ('Remaning Balance: ' , budget_amount - gas_budget - hotel_budget - food_budget)
