choice = "n"

def add(x,y):
    return x+y

def substract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def process_input(operation,x,y):
    match operation:
        case "+":
            return add(x,y)
        case"-":
            return substract(x, y)
        case "*":
            return multiply(x,y)
        case "/":
            return divide(x,y)

while choice != "exit":
    if choice == 'n':
        current_calculation = float(input("What's the first number?: "))
    operation = input("+\n-\n*\n/\nPick an operation: ")
    next_number = float(input("What's the next number?: "))
    current_calculation = process_input(operation,current_calculation,next_number)
    choice = input(f"Type 'y' to continue calculating with {current_calculation}, or type 'n' to start a new calculation or 'exit' to stop the program: \n")


