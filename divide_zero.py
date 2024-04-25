
def divide_2_numbers():
    """Ask the user for 2 numbers to divide them """

    while True:

        numerator = input("What is the first number?")
        if numerator == "q":
            break

        denominator = input("What is the 2nd number?")
        if denominator == "q":
            break

        try:
            result = int(numerator)/int(denominator)
        except :
            print("Cannot divide by these numbers")
        else:
            print(result)


divide_2_numbers()