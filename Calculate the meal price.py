meal_cost = float(input("Enter the meal cost :- "))
tip_percent = int(input("Enter the tip percent :- "))
tax_percent = int(input("Enter the tax percent :- "))
tip = (meal_cost * tip_percent) / 100
tax = (meal_cost * tax_percent) / 100
total_cost = meal_cost + tip + tax
print(round(total_cost))
