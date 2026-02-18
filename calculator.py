def calculator():
    try:
        # Taking inputs
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("\nChoose Operation")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        choice = input("Enter your choice (1/2/3/4): ")

        # Performing operations
        if choice == '1':
            print("Result:", num1 + num2)

        elif choice == '2':
            print("Result:", num1 - num2)

        elif choice == '3':
            print("Result:", num1 * num2)

        elif choice == '4':
            if num2 == 0:
                print("Error: Division by zero is not allowed")
            else:
                print("Result:", num1 / num2)

        else:
            print("Invalid choice")

    except ValueError:
        print("Error: Please enter valid numbers")

    # Ask user if they want to continue
    again = input("\nDo you want to calculate again? (yes/no): ")

    # Recursion call
    if again.lower() == "yes":
        calculator()
    else:
        print("Calculator Closed")


# Function Call
calculator()
