
max_columns = 10
min_columns = 2

lower = 33
upper = 127

char = input("Enter a character: ")
print("The ASCII code for {} is {}".format(char, ord(char)))
number = int(input("Enter a number between {} and {}: ".format(lower, upper)))
while number < lower or number > upper:
    number = int(
        input("Enter a number between {} and {}: ".format(lower, upper)))

print("The character for {} is {}".format(number, chr(number)))
for value in range(lower, upper + 1):
    print("{:3} {:>4}".format(value, chr(value)))

columns = int(input("Enter number of columns: "))
while columns < min_columns or columns > max_columns:
    print("use a value between {} and {}".format(min_columns, max_columns))
    columns = int(input("Enter number of columns: "))

number_of_values = upper - lower + 1
rows = number_of_values // columns

print("V1: Horizontal to vertical ordering")
value = lower
for row in range(rows):
    for column in range(columns):
        print("{:6} {:>2}".format(value, chr(value)), end="")
        value += 1
    print()
start_value = value
for value in range(start_value, upper + 1):
    print("{:6} {:>2}".format(value, chr(value)), end="")
print("\n")
print("Version 2: Vertical to horizontal ordering")
for row in range(rows + 1):
    start_value = lower + row
    value = start_value
    for column in range(columns - 1):
        value_to_print = value + (column * rows)
        print("{:6} {:>2}".format(value_to_print, chr(value_to_print)), end="")
        value += 1
    value_to_print = value + ((column + 1) * rows)
    if value_to_print <= upper:
        print("{:6} {:>2}".format(value_to_print, chr(value_to_print)), end="")
    print()
