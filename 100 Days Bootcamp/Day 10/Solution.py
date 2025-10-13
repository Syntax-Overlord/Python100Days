art = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

# result = 0


def add(a, b):
    result = a + b
    return result


def subtract(a, b):
    result = a - b
    return result


def multiply(a, b):
    result = a * b
    return result


def divide(a, b):
    result = a / b
    return result


def calculator():
    print(art)
    result = 0
    numOne = float(input("What's the first number?: "))
    operation = input("+\n-\n*\n/\nPick an operation: ")
    numTwo = float(input("What's the second number?: "))
    match operation:
        case "+":
            result = add(numOne, numTwo)
        case "-":
            result = subtract(numOne, numTwo)
        case "*":
            result = multiply(numOne, numTwo)
        case "/":
            result = divide(numOne, numTwo)
    print(f"{numOne} {operation} {numTwo} = {result}")
    while (
        input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: "
        )
        == "y"
    ):
        numOne = result
        operation = input("+\n-\n*\n/\nPick an operation: ")
        numTwo = float(input("What's the next number?: "))
        match operation:
            case "+":
                result = add(numOne, numTwo)
            case "-":
                result = subtract(numOne, numTwo)
            case "*":
                result = multiply(numOne, numTwo)
            case "/":
                result = divide(numOne, numTwo)
        print(f"{numOne} {operation} {numTwo} = {result}")


calculator()
