# Example 1
# range(begin, end, step)
# value is printed till 1 value before given in end place
# step is optional
# below prints value of i in vertical line
for i in range(1, 10) :
    print(i)

print("*****")

# Example 2
# below prints value of i in horizontal line
for i in range(1, 10) :
    print(i, end = " ")

print("*****")

# Example 3
# below prints value of i in vertical line, step means next plave value to jump on
# 1, 1+2 = 3, 3+2 = 5, 5+2 = 7, 7+2 = 9
for i in range(1, 10, 2) :
    print(i, end = " ")

print("*****")

# Example 4
# 10 will be considered as end
# 0 will be considered as default value for begin if only 1 value is provided in range
for i in range(10) :
    print(i, end = " ")

print("*****")

# Example 5
# Get factorial of a number
num = int(input("Enter the number to get it's factorial "))
fact = 1
for i in range(1, num + 1) :
    fact = fact * i

print("The factorial of", num, "is:", fact)