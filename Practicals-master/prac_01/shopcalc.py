total = []
print("Welcome to the Shop Calculator")
itemAmount = int(input('How many items would you like to calculate: '))
for i in range(itemAmount):
    numbers = float(input('Enter number '))
    total.append(numbers)
for elem in total:
    print ("price of item: ", elem)
final = sum(total)
if final >= 100:
    bonus = final * 0.10
    final = bonus + final
    print("The total amount for your", itemAmount, "items are: ",  final, "(10% discount applied)")
else:
    print("The total amount for your", itemAmount, "items are: ",  final, "(No discount applied)")

