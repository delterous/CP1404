"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
if score in range(90,101):
    print("Excellent")
elif score in range(0,50):
    print("Bad")
elif score in range(50,90):
    print("Passable")
elif score >= 100:
    print("Invalid score")
else:
    print("Invalid score")
