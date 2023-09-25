# Function to validate integer input
def valueValidate(prompt):
    while True:
        user_input = input(prompt)
        try:
            value = int(user_input)
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Function to validate operation input
def operationsValidate(prompt):
    validOperations = ['+', '-', '*', '/']
    while True:
        operation = input(prompt)
        if operation in validOperations:
            return operation
        else:
            print("Invalid operation. Please enter one of +, -, *, /.")


 # Input validation and data retrieval
    values = [valueValidate("Enter the first integer: "),
              valueValidate("Enter the second integer: "),
              valueValidate("Enter the third integer: ")]
    operations = [operationsValidate("Enter the first operator (+, -, *, /): "),
                  operationsValidate("Enter the second operator (+, -, *, /): ")]

