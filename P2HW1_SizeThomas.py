#Travel expense calculator
#October 7, 2022
#CTI-110 P2HW1 - Travel Expense
#Thomas Size
#this program takes input on various aspects of a travel budget and calculates total expenses

#get user budget input

print ('This program calculates and displays travel expenses')
budget_amount = float(input('Enter Budget: '))
destination = input('Enter destination: ')
gas_budget = float(input('How much will you spend on gas? '))
hotel_budget = float(input('How much will you spend on lodging? '))
food_budget = float(input('How much will you spend on food? '))
remaining_balance = float(budget_amount - gas_budget - hotel_budget - food_budget)

#format input for display

budget_amount_dollars = '${:.1f}'.format(budget_amount)
gas_budget_dollars = '${:.1f}'.format(gas_budget)
hotel_budget_dollars = '${:.1f}'.format(hotel_budget)
food_budget_dollars = '${:.1f}'.format(food_budget)
remaining_balance_dollars = '${:.1f}'.format(remaining_balance)

#displays input before calculating

print()
print ('------------Travel Expenses------------')
print (f'Location: {destination: >24}')
print (f'Initial budget: {budget_amount_dollars: >16}')
print (f'Fuel: {gas_budget_dollars: >25}')
print (f'Accomodation: {hotel_budget_dollars: >17}')
print (f'Food: {food_budget_dollars: >25}')
print ('---------------------------------------')

#displays final calculation

print (f'Remaning Balance:  {remaining_balance_dollars:>12}')
