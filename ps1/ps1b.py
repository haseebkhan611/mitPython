annual_salary=75000
portion_saved=.05
total_cost=1500000
annual_raise=0.05
down_payment=0.25
annual_return=0.04

portion_down_payment=down_payment*total_cost

current_savings=0
monthly_savings = 0
months=0

while(current_savings<=portion_down_payment):
    months = months + 1
    if (months%6==0):
        annual_salary=annual_salary+(annual_salary*annual_raise)
    current_savings=current_savings+(current_savings*(annual_return/12))
    monthly_salary = int(annual_salary / 12)
    monthly_savings = monthly_salary * portion_saved
    current_savings = current_savings + monthly_savings




print("Number of months : "+str(months))
print(str(monthly_savings))