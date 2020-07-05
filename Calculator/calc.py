# Here we are importing the file name operators
import operators

# Here we are creating a class called calc
class calc:

    print("Please select what you want to do:")
    print("1 - Calculator")
    print("2 - Area of triangle")
    print("3 - Inches to CM converter")

    choice = int(input("Please choose what you want to do: "))



    # Here we are getting the user input for an integer
    num1 = int(input("Please enter an integer: "))

    # Here we are getting the user input for an integer
    num2 = int(input("Please enter an integer: "))

    # Here we are prompting the user to make a choice on the operators
    print("Choose a operator that you want to use")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("5 - Remainder")

    # Here the user is required to select an operator based on the previous options
    operator_choice = int(input("Please enter the operator you would like to use: "))

    # This is the control flow relating the users input to which operator will be used
    if operator_choice == 1:
        print(operators.add_values(num1, num2))
    elif operator_choice == 2:
        print(operators.minus_values(num1, num2))
    elif operator_choice == 3:
        print(operators.multiply_values(num1, num2))
    elif operator_choice == 4:
        print(operators.divide_values(num1, num2))
    elif operator_choice == 5:



    else:
        print("Error")



