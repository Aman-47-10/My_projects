# Class of a simple calculator
class Calculator:
    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero is not allowed"

# Function to handle valid number input
def get_number_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.lower() == 'q':
            return None  # Allows quitting with 'q'
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number or 'q' to quit.")

# Welcome panel
print("Welcome to the calculator!")

# Choice panel between long and short operation
print("""
Enter 1 for long operation
Enter 2 for operation between two numbers
""")
try:
    choice = int(input("Enter your command: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

calculator = Calculator()  # Create an instance of the Calculator class

if choice == 2:
    # Short operation (two numbers)
    print("You can perform addition, subtraction, multiplication, or division.")
    print("Enter 'q' to quit the operation.")
    while True:
        # Ask for the first number
        a = input("Enter the first number: ")
        if a.lower() == 'q':
            break
        try:
            a = float(a)
        except ValueError:
            print("Invalid input. Please enter a valid number or 'q' to quit.")
            continue

        # Ask for the operation
        operation = input("Enter the operation (+, -, *, /): ")

        # Ask for the second number
        b = input("Enter the second number: ")
        if b.lower() == 'q':
            break
        try:
            b = float(b)
        except ValueError:
            print("Invalid input. Please enter a valid number or 'q' to quit.")
            continue

        # Perform the calculation based on the chosen operation
        if operation == "+":
            print(f"The result is {calculator.addition(a, b)}")
        elif operation == "-":
            print(f"The result is {calculator.subtraction(a, b)}")
        elif operation == "*":
            print(f"The result is {calculator.multiplication(a, b)}")
        elif operation == "/":
            print(f"The result is {calculator.division(a, b)}")
        else:
            print("Invalid operation. Please choose from (+, -, *, /).")

elif choice == 1:
    # Long operation (result carries forward)
    print("""
    Enter 1 for addition
    Enter 2 for subtraction
    Enter 3 for multiplication
    Enter 'q' to quit
    """)

    # Ask the user for the operation they want to perform
    operation = input("Enter the operation (1 for addition, 2 for subtraction, 3 for multiplication, 'q' to quit): ").lower()

    if operation == 'q':
        print("Exiting the program.")
        exit()

    if operation not in ['1', '2', '3']:
        print("Invalid input. Please enter 1, 2, or 3.")
        exit()

    # Initialize result
    result = 0
    skip = False  # To track if the first number is set

    # Perform operation continuously
    while True:
        number = get_number_input("Enter a number: ")
        if number is None:
            break  # Exit the loop if 'q' is entered

        if not skip:
            result = number  # Set result to the first number
            skip = True
        else:
            if operation == '1':  # Addition
                result = calculator.addition(result, number)
            elif operation == '2':  # Subtraction
                result = calculator.subtraction(result, number)
            elif operation == '3':  # Multiplication
                result = calculator.multiplication(result, number)

        print(f"Current result is: {result}")

    # Final result after exiting the loop
    print(f"The final result is: {result}")
else:
    print("Invalid choice. Please enter 1 or 2.")
