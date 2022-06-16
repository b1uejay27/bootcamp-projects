def main():
    age = int(input("What is your age?\n"))
    newage = age + 10
    print("You will be " + str(newage) + " in 10 years")

def othermain():
    first_number = float(input("Input a number:\n"))
    second_number = float(input("Input another number:\n"))
    print(str(first_number) + " plus " + str(second_number) + " equals " + str(first_number + second_number) + ".")
    print(str(first_number) + " minus " + str(second_number) + " equals " + str(first_number - second_number) + ".")
    print(str(first_number) + " multiplied by " + str(second_number) + " equals " + str(first_number * second_number) + ".")
    print(str(first_number) + " divided by " + str(second_number) + " equals " + str(first_number / second_number) + ".")


main()
othermain()