# -*- coding: utf-8 -*-
# Problem Set 1B
# Name: Xudong Sun
# Collaborators: NA
# Time Spent: 0:13

# ask the user to enter the annual salary, 
# portion of salary to be saved,
# and total cost of the house
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))
# additionally, semi-annual raise
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: '))



# other variables, current savings, annual return rate, 
current_savings = 0
r = 0.04
# and portion of the cost for a down pament
portion_down_payment = 0.25


# down_payment:
down_payment = total_cost * portion_down_payment

# calculate the number of months(month_needed) using a while loop
month_needed = 0
while current_savings < down_payment:
    # if not enough, add one more month
    # with its returns(current_savings*r/12), 
    # and monthly saving(portion_saved*annual_salary/12)
    # every 6 month, the annual salary will increase
    if month_needed >= 6 and month_needed % 6 == 0: 
        annual_salary *= (semi_annual_raise + 1)
        current_savings += current_savings * r / 12 + portion_saved * annual_salary / 12
        month_needed += 1
    else:
        current_savings += current_savings * r / 12 + portion_saved * annual_salary / 12
        month_needed += 1
 
# until current_savings >= down_payment   
print('Number of months: ', month_needed)
















