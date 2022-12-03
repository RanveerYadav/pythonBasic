"""
    DataTypes
    -------------
    Mutable:
        List, Dictionaries and Sets
    Immutable:
        Strings, Numbers and Tuples
    ------------
    Mutable means cannot be changed directly
"""
# List (basic array)
# Example 1
list = [1, 2, "Ranveer"]
print(list)
print(list[1])

# Example 2
multiList = [
    [1, 2, 3],
    [5, 6, 7],
    [8, 9, 0],
]
print(multiList[2][1])

# Dictionaries (associative array)
dict = {'name':'Ranveer', 'color':'red', 'country':'India', 'continent':'Asia'}
print(dict['country'])

# Files
# Create a new file and write in the new file
f = open('16a. File.txt', 'w')
f.write('Hello File')
f.write('\nSecond comment')
f.close()
# Open the created file and read content from the file
r = open('16a. File.txt')
text = r.read()
print(text)

# Tuples
tuple = (1, 2, 'Ranveer')
print(tuple)
print(tuple[1])