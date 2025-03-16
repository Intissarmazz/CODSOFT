while True:
    print("_____Welcome to the calculator made by Maaziz Intissar_____")
    try:
        a = float(input("Please enter the first number: "))
    except ValueError:
        print("Please enter a valid number!")
        continue
    try:
        op = input("Please choose the desired operation ( +, -, *, / ): ")
    except ValueError:
        print("Please enter a valid operation!")
        continue
    try:
        b = float(input("Please enter the second number: "))
    except ValueError:
        print("Please enter a valid number!")
        continue
    if op == "+":
        print("The result is:", a + b)
    elif op == "-":
        print("The result is:", a - b)
    elif op == "*":
        print("The result is:", a * b)
    elif op == "/":
        if b == 0:
            print("The operation is impossible, the divisor must be different from 0")
        else:
            print("The result is:", a / b)
    else:
        print("Invalid operation")
    restart = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if restart != "yes":
        print("Thank you for using the calculator!")
        break












