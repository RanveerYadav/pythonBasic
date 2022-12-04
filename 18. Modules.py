# Import entire sys module
import sys
# Import only pi from math module
from math import pi
# Giving alias
from math import sqrt as squareRoot
# Import custom module created
from MyModule import multiply
# Import random module
import random
import math

print(sys.path)
print("Value of PI =", pi)
print("Square root =", int(squareRoot(81)))
print(multiply(int(10), int(5)))
randomNum = random.random()
print(randomNum)

# Generate OTP logic
def generateOTP() :
    OTP = ''
    for i in range(1, 5) :
        randomNumber = random.random()
        roundNumber = math.floor(randomNumber * 10)
        # Below line will work same as above line
        # roundNumber = int(randomNumber * 10)
        OTP += str(roundNumber)
    return OTP

print(generateOTP())

