"""
Program to calculate and display a user's bonus based on the sales
if sales are under $1000, the user gets a 10% bonus.
If sales are $1000 or over, the bonus is 15%
"""


sales = float(input("Enter sales: $"))
if sales < 1000 > 0:
    bonus = sales * 0.10
    print("bonus: $", bonus)
else:
    bonus = sales * 0.15
    print("bonus: $", bonus)
