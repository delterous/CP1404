MIN_LENGTH = 2
MAX_LENGTH = 6


def main():
    #print("Please enter a valid password")
    #print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          #"characters.")
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password), password))
    print("*" * len(password))


def is_valid_password(password):
    count_lower = 0
    count_upper = 0
    count_digit = 0
    for char in password:
        if char.isdigit():
            count_digit += 1
        elif char.isupper():
            count_upper += 1
        elif char.islower():
            count_lower += 1
    if count_lower == 0 or count_upper == 0:
        return False
    return True


main()
