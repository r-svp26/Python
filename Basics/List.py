x = [1, 2, 4, 8, 9]
print(x[1])

# List Manipulation
x.append(10)
x.insert(2, 90)
x.remove(4)
x.remove(x[4])
print(x)
# List Slicing
print(x[2:5])
# Last Element
print(x[-1])
# Second Last Element
print(x[-2])
print(x.index(1))
# Count the element occurrence
print(x.count(10))

# Sorting the list
x.sort()
print(x)

# Two Dimensional List
y = [[2, 4], [5, 4], [10, 6]]
print(y)
print(y[1])
