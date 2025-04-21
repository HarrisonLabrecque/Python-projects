def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b == 0:
        print("Can't divide by zero.")
        return None
    return a / b

useCalc = True
print("Welcome to the basic calculator.")

while useCalc:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue

    while True:
        print("\nHere is a list of operations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        

        try:
            option = int(input("Choose an operation: "))
        except ValueError:
            print("Invalid option. Please enter a number.")
            continue

        match option:
            case 1:
                res = add(num1, num2)
                print("Result:", round(res, 2))
            case 2:
                res = sub(num1, num2)
                print("Result:", round(res, 2))
            case 3:
                res = mult(num1, num2)
                print("Result:", round(res, 2))
            case 4:
                res = div(num1, num2)
                if res is not None:
                    print("Result:", round(res, 2))
            

    again = input("Do you want to perform another operation on the same numbers? (y/n): ").strip().lower()
    if again != 'y':
            useCalc = False
            break  
            
