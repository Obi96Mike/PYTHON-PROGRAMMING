# A tuple is similar to a list in that it stores a collection of elements. 
# Like lists, you can access individual elements in a tuple using their indices but you cannot modify or change these elements.
# It is an immutable object; same as int, float, bool, string.

# tuple indexing
tup = (1, 2, 3)
print (tup[1])
print(tup[-1])

x[0] = 2 # raises an exception

# in operator
contains = 4 in x
print(contains)

# Nested Tuples
x = (1, 2, 3, (1, 2), True, [])
print(x[3])

# Adding Tuples
x = (1, 2)
y = (3, 4)

# Multiplying tuples
combined = [1] * 2
print (combined)