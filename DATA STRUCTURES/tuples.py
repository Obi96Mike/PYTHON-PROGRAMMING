tuple() # fixed length immutable list.
# Tuples can hold homogenous data but in real life programs, they are used for heterogenous data; data of a variety of different types.
# e,g representing a user on a website with a tuple of 3 values like a string for user's name, number for their age and boolean to represent whether they are a subscriber or not.

# A tuple is similar to a list in that it stores a COLLECTION of elements; parentheses is used to define it.
# Like lists, you can access individual elements in a tuple using their indices but you cannot modify or change these elements.
# It is an immutable object; same as int, float, bool, string.
# Read-only list; we cannot use it to contain a sequence of objects but we cannot modify sequence or existing object/ add any object to it/ remove an existing object
# Once a tuple is made, you cannot modify or mutate it. You cannot remove items, add items.

empty = ()
print(type(empty)) 

# 1 element tuple
x = (1, )
print(x)

# tuple indexing. Similar to lists, we can access individual items using an index.
tup = (1, 2, 3, True, "str")
print (tup[1]) # output is 2
print(tup[-1]) # output is "str"
print(tup[0:2]) # getting range of items

# tup[1] = 0  raises an exception (Type error); tuples can't be modified.

# len() function
print(len(tup))

# .count() method - counting how may times an element occurs in a tuple
count = tup.count(1) # counting how many times 1 occurs
print(count)

# .index() method
index = tup.index(1) # gives index of the 1st occurrence of whatever element that we are looking for
print(index)

# in operator - to check if something is contained in tuple 
contains = 4 in tup
print(contains)

# Nested Tuples
x = (1, 2, 3, (1, 2), True, [])
print(x[3])
print(x[3][0]) # accessing 1st element in nested tuple

# Adding Tuples/ Lists
x = (1, 2)
y = (3, 4)
combine = x + y
print(combine)

# Multiplying tuples/ lists
combined = [1, 2] * 2
print (combined)


# Create a faves variable with a list of your 3 three favorite movies as strings. 
# Use the tuple function to convert the list to a tuple and save the result in a movies variable.
faves = ['Poo', 'Hoo', 'Koo']
movies = tuple(faves)
