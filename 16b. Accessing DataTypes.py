############ List #############
# Example 1: for loop
list = [10, 20, 30, 40, 50, 60]
for i in list :
    print(i)

print('-----')
# Example 2: Get length and loop
n = len(list)
for i in range(n) :
    print(list[i])

print('-----')
# Example 3: Delete 1 element and check others
del list[0]
print(list)

print('-----')
list = [10, 20, 30, 40, 50, 60, 20, 10, 20]
# Example 4: Inbuilt function
print(list)
print(list.index(50))
print(list.count(20))
list.append(100)
print(list)
print(list.remove(20))
print(list)

############ Files #############
"""
    Modes in file
    ---------------
    r: read
    w: write
    a: append
    r+: read + write
"""

############ Dictionaries #############
# Example 1
dic = {'1':'One', '2':'Two'}
print("without dict method ", dic)

# Example 2
dic = dict({'1':'One', '2':'Two'})
print("with dict method ", dic)

# Example 2
dic = dict([('1', 'One'), ('2','Two')])
print("dict in form of pairs ", dic)