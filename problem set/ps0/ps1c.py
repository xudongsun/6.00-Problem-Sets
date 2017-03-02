# -*- coding: utf-8 -*-
# Problem Set 1B
# Name: Xudong Sun
# Collaborators: NA
# Time Spent: 0:40

# ask the user to enter the annual salary, 
annual_salary_input = float(input('Enter your annual salary: '))

# additionally, semi-annual raise
semi_annual_raise = 0.07


# other variables, current savings, annual return rate, 
current_savings = 0
r = 0.04
# and portion of the cost for a down pament
portion_down_payment = 0.25

# down_payment:
total_cost = 1000000
down_payment = total_cost * portion_down_payment

error = 100
# a function to calculate the number of months, like ps1b.py
def n_months(current_savings, annual_salary, portion_saved):
                 
    month_needed = 0
    while abs(current_savings - down_payment) > error:
        # if not enough, add one more month
        # with its returns(current_savings*r/12), 
        # and monthly saving(portion_saved*annual_salary/12)
        
        if month_needed >= 6 and month_needed % 6 == 0: 
            annual_salary *= (semi_annual_raise + 1)
            # every 6 month, the annual salary will increase
            current_savings += current_savings * r / 12 + portion_saved * annual_salary / 12
            month_needed += 1
        else:
            current_savings += current_savings * r / 12 + portion_saved * annual_salary / 12
            month_needed += 1
    return(month_needed)
    

# exclude the "impossible" stuation
if n_months(0, annual_salary_input, 1) > 36:
    print('It is not possible to pay the down payment in three years.')

else: # use bisection research

    top = 10000
    down = 0
    
    steps = 0    
    
    while top != down:
        mid = (top + down)//2
        # calculate the number of months with the guess
        # reset variables before every trial
        n = n_months(0, annual_salary_input, mid/10000)
        
        # if the guess is right
        if n == 36:
            print('Best savings rate: ', mid/10000)
            break
        # if th number of months is greater than 36
        # the portion saved should be increased
        elif n < 36:
            top = mid
        # and vise versa
        else:
            down = mid
            
        #count the step
        steps += 1
        
print('Steps in bisection search: ', steps)
    

