import operators

class calc:


    num1 = int(input("Please enter an integer: "))
    num2 = int(input("Please enter an integer: "))


    print("Choose a operator that you want to use")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")

    operator_choice = int(input("Please enter the operator you would like to use: "))

    if operator_choice == 1:
        print(operators.add_values(num1, num2))
    elif operator_choice == 2:
        print(operators.minus_values(num1, num2))
    elif operator_choice == 3:
        print(operators.multiply_values(num1, num2))
    elif operator_choice == 4:
        print(operators.divide_values(num1, num2))
    else:
        print("Error")



