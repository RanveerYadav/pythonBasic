'''
    and: T + T = T
    or:  F + F = F
    not: not(T) = F, not(F) = T
'''

num1 = 10
num2= 20
num3= 30

print((num1 < num2) and (num2 < num3))
print((num1 < num2) or (num2 > num3))
print(not(num1 < num2))
print(not(num1 > num2))