#program 1 and 2

name = input("Enter your name: ")
f = open("name.txt", "a")
f.writelines(name + '\n')
print("Your name is", name)
f.close()

#program 3

file = open("numbers.txt", "r")
number1 = int(file.readline())
number2 = int(file.readline())
print(number1 + number2)
file.close()

#program 4

file = open("numbers.txt", "r")
total  = 0
for line in file:
    number = int(line)
    total += number
print(number)
file.close()
