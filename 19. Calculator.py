num1 = int(input("Enter number 1 "))
num2 = int(input("Enter number 2 "))

print("""Please enter 1 for addition, 2 for subtraction, 3 for multiplication and
    4 for division""")

operation = int(input("Enter operation to be performed "))

def calculate(num1, num2 , operation) :
    if (operation == 1) :
        return add(num1, num2)
    elif (operation == 2) :
        return subtract(num1, num2)
    elif (operation == 3) :
        return multiply(num1, num2)
    else :
        return division(num1, num2)

def add(num1, num2) :
    return num1 + num2

def subtract(num1, num2) :
    return num1 - num2

def multiply(num1, num2) :
    return num1 * num2

def division(num1, num2) :
    return num1 // num2

result = calculate(num1, num2, operation)
print("The answer is", result)