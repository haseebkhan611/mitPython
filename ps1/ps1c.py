
# portion_saved=.05
total_cost=1000000
annual_raise=0.07
down_payment=0.25
annual_return=0.04
current_savings=0
monthly_savings = 0
months=0
annual_salary=120000

portion_down_payment=down_payment*total_cost
monthly_salary = int(annual_salary / 12)

steps = 0
high = 1.0
low = 0.0
guess = (high+low)/2.0
total_salaries = 0.0
tolerance = 100

def curSavings(guess):
    while(current_savings<=portion_down_payment):
        months = months + 1
        if (months%6==0):
            annual_salary=annual_salary+(annual_salary*annual_raise)
        current_savings=current_savings+(current_savings*(annual_return/12))
        monthly_salary = int(annual_salary / 12)
        monthly_savings = monthly_salary * guess
        current_savings = current_savings + monthly_savings
    return current_savings
print("Number of months : "+str(months))
print(str(monthly_savings))