starting_salary = 100000  # Assuming Annual Salary of 100k
months_salary = starting_salary/12
total_cost = 1000000.0
semi_annual_rate = .07
investment_return = 0.04
down_payment = total_cost * 0.25
print("down payment: ", down_payment)
r = 0.04
current_savings = 0.0
#months = 36
tolerance = 100
steps = 0
high = 1.0
low = 0.0
guess = (high+low)/2.0
total_salaries = 0.0
tolerance = down_payment/100 # I chose this tolerance to say if my savings are between [down_payment - (downpayment + down_payment/100)]  result is admissible. (this is quite a high tolerance but you can change at leisure)
def calSavings(current_savings,months_salary,guess):
    for months in range(0,37):
        if  months%6==1 and months >1:
            months_salary=months_salary*(1+semi_annual_rate)
        current_savings = current_savings + months_salary * guess
    current_savings = current_savings * (1+0.04)
    return(current_savings)

while abs(current_savings-down_payment)>=100:
    current_savings = calSavings(current_savings,months_salary,guess)
    if  current_savings < down_payment:
        low = guess
        current_savings = 0.
    elif current_savings > down_payment + tolerance:
        high = guess
        current_savings = 0.
    if (steps > 100):  # I chose a maximum step number of 100 because my tolerance is high
        print("It is not possible to pay the down payment in three years.")
        break
    guess = (low + high) / 2
    steps = steps + 1

print("Best saving rate: ", guess)
print("With current savings: ", current_savings)
print('Number of steps '+str(steps))