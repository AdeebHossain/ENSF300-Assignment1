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
          
#Function to display the expression and result
def display(number_list, operator_list,):

    number_list_copy = number_list.copy()
    operator_list_copy = operator_list.copy()
    logic(number_list_copy, operator_list_copy)  # Evaluate the expression first
    result = num_list_copy

    # Construct a formatted expression string

    print(f'Result: {result}')

# Function to perform addition
def myAdd(a, b):
    return a + b

# Function to perform subtraction
def mySub(a, b):
    return a - b

# Function to perform multiplication
def myMul(a, b):
    return a * b

# Function to perform division
def myDiv(a, b):
    return a // b

def logic(num_list, op_list):
    while '/' in op_list or '*' in op_list:
            if '/' in op_list:
                index = op_list.index('/')
                result = myDiv(num_list[index], num_list[index + 1])
                num_list[index] = result
                del num_list[index + 1]
                del op_list[index]
            elif '*' in op_list:
                index = op_list.index('*')
                result = myMul(num_list[index], num_list[index + 1])
                num_list[index] = result
                del num_list[index + 1]
                del op_list[index]

        # Evaluate addition and subtraction
    while '+' in op_list or '-' in op_list:
        if '+' in op_list:
            index = op_list.index('+')
            result = myAdd(num_list[index], num_list[index + 1])
            num_list[index] = result
            del num_list[index + 1]
            del op_list[index]
        elif '-' in op_list:
            index = op_list.index('-')
            result = mySub(num_list[index], num_list[index + 1])
            num_list[index] = result
            del num_list[index + 1]
            del op_list[index]

if __name__ == "__main__":
    
 # Input validation and data retrieval
    values = [valueValidate("Enter the first integer: "),
              valueValidate("Enter the second integer: "),
              valueValidate("Enter the third integer: ")]
    operations = [operationsValidate("Enter the first operator (+, -, *, /): "),
                  operationsValidate("Enter the second operator (+, -, *, /): ")]
  
    display(values, operations)
