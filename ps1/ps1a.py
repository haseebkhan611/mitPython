
# annual_salary=float(input("Enter your annual salary : "))
# portion_saved=float(input("Enter the percent of your salary to save, as a decimal : "))
# total_cost=float(input("Enter the cost of your dream home : "))
annual_salary=(165000*12)
portion_saved=.20
total_cost=10000000

monthly_salary=int(annual_salary/12)
portion_down_payment=0.50*total_cost
monthly_savings=monthly_salary*portion_saved
current_savings=0

months=0

while(current_savings<portion_down_payment):
    months=months+1
    current_savings=current_savings+(current_savings*(.04/12))
    current_savings = current_savings + monthly_savings

print("Number of months : "+str(months))
print(str(monthly_savings))