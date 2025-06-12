def calculator():
    while True:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /):  ")

        if operation == "+":
            print(num1 + num2)
        elif operation == "-":
            print(num1 - num2)  
        elif operation == "*":
            print(num1 * num2)
        elif operation == "/":
            if num2 == 0:
                print("Math Error")
            else:
                print(num1 / num2)
        else:
            print("Invalid operation. Please try again.")
            continue

        choose = input("Do you want to calculate again? (yes/no): ")
        if choose == "yes":
            return calculator()
        elif choose == "no":
            print("Thank you for using the calculator!")
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")
            return  choose
calculator()