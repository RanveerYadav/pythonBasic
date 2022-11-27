# Example 1
num1 = 13
num2 = 10

if (num1 > num2) :
    print("Yes num1 is greater than num2")

# Example 2
age = int(input("Enter your age: "))
if (age > 18) :
    print("You are eligible for voting")

# # Example 3, script to know value is alpha or digit
value = input("Enter the value: ")
if (value.isalpha()) :
    print("Entered value is an alphabet")

if (value.isdigit()) :
    print("Entered value is digit")