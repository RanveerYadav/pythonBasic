# printing design pattern
'''
    Print the following design pattern
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
    rows = 5 = i, range(1, 6)
    max col elements = 5, j = i + 1, range (1, i+1)
'''
for i in range(1,6) :
    for j in range(1, i+1) :
        print(j, end = " ")
    print("\r")

'''
    Above logic
    i = 1, j = [1]
    i = 2, j = [1,2]
    i = 3, j = [1,2,3]
    "
    "
'''