annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("The portion of salary to be saved: "))
total_cost = float(input("The cost of your dream home: "))

portion_down_payment = total_cost * 0.25
current_savings = 0
""" r = 0.04
annual_return = current_savings*r/12 """
months = 0

while(current_savings < portion_down_payment):
    current_savings += (round(annual_salary / 12)) * portion_saved
    current_savings += round(current_savings * 0.04 / 12)
    months = months + 1
print(months, current_savings)
