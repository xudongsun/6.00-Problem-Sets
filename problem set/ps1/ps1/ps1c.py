# -*- coding: utf-8 -*-
# Problem Set 1B
# Name: Xudong Sun
# Collaborators: NA
# Time Spent: 0:40

# ask the user to enter the annual salary, 
annual_salary = float(input('Enter your annual salary: '))

# additionally, semi-annual raise
semi_annual_raise = 0.07


# other variables, current savings, annual return rate, 
current_savings = 0
r = 0.04
# and portion of the cost for a down pament
portion_down_payment = 0.25

# down_payment:
total_cost = 1000000

# use bisection research

# basic values
top = 10000
down = 0
    
steps = 0    
print_b = True 
   
# error of trial
error = 100
    
while abs(total_cost * portion_down_payment - current_savings) > error:
    # proportion of saving, guess
    mid = (top + down)//2
    portion_saved = mid/10000
      
    # reset the basic values
    current_savings = 0
    monthly_salary = annual_salary/12    
    
    # try the estimate portion
    n_month = 0 
    while n_month < 36:
        
        current_savings += current_savings * r / 12 + portion_saved * monthly_salary
        n_month += 1
        # every 6 month, the annual salary will increase
        if n_month % 6 == 0:
            monthly_salary *= (semi_annual_raise + 1)
        
    # adjustment: more or less after 36 months?
    if current_savings - total_cost * portion_down_payment > 0:
        top = mid
    # vise versa
    elif current_savings - total_cost * portion_down_payment < 0:
        down = mid
            
    
    #count the step
    steps += 1
    
    # for impossible situation: 
    # as there is no integer between 9999 and 10000
    # if 'down' is up to 9999, we take it as impossible
    if down == 9999:
        print('It is not possible to pay the down payment in three years.')
        print_b = False
        break
    
if print_b == True:
    print('Best savings rate: ', portion_saved)        
    print('Steps in bisection search: ', steps)

    

