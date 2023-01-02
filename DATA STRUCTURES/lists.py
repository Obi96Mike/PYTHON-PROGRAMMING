# Lists is a mutable data type that stores ordered sequence of objects [strings, numbers, booleans, lists]; called an array in other programming languages.

# Lists of strings
letters = ['a', 'b', 'c', 'd', 'e', ]

# Lists of numbers; 100 zeros
zeros = [0] * 100

# List of lists
matrix = [[0, 1], [2, 3]]

numbers = list(range(20)) # list function takes an iterable. You can pas any iterable and convert it to a list. 
# Range function returns a range object that is iterable.
print(numbers[::-1]) # returns all item in original list in reverse order; increments of 1 but from end of list to beginning of list.

chars = list("Hello World") # Strings are iterable. 
print(len(chars))

# METHOD -  A function that belongs to an object.
# It is bound to a specific instance/object and is invoked using dot syntax followed by a pair of parentheses.
# Just like a regular function, a method may or may not accept arguments.

# ACCESSING ITEMS IN A LIST
letters = ["a", "b", "c", "d", "e", "f"]
print(letters[-1]) # returns 1st item from end of list
print(letters[0]) # returns 1st item in list
letters[0] = "A" # modifying item in list; assigning new value at index position
letters[0:3] # using 2 indexes to slice a list. Returns a new list with 1st 3 items in original list
letters[0:] # excluding end index
letters[:3] # excluding start index
letters[::2] # slicing a list including a step; useful in situations where you wan to return every 2nd or 3rd element in original list.

lst = [[5,5,[100]], [2,3], [1,2,3]] # Accessing items in interior list (multidimensional list/ nested list - lists inside other lists)
print(lst[-1][1])
print(lst[0][2][0])


# ADDING ITEMS TO LIST(S) / COMBINING LISTS TOGETHER
# Plus sign to concatenate multiple lists.
combined = zeros + letters
x = [1, 2, 3]
y = [1, 2]
combined = x + y
print(combined)

# extend method - allows us to add multiple elements to a list in a single method call; modify x such that it contains all elements of y at the end of the list.
x.extend(y)  # extend x
print(x)
y.extend(x)  # extend y
print(y)
letters = ['a', 'b', 'c', 'd', 'e', 'f']
letters.extend(['d', 'e', 'f'])
# append method - adds a single element/object/item at end of a list.
letters.append("d")
print(letters)
# insert method - adds/ inserts item/element at a specific index position.
letters.insert(0, '-')
print(letters)


# REMOVING ITEMS
# removes item at end of list and returns element that has been removed.
letters.pop()
# pass an index to pop method to remove an item at a given index.
letters.pop(0)
# removes an element / object from a list by its value; not by its index position.
# removes first occurence of b. If you have multiple b's, only the first will be removed.
letters.remove('b')
# deletes item by index
del letters[0]
# deletes range of items
del letters[0:3]
# removes all objects in a list
letters.clear()
# removes all objects / elements from a list reducing list's length to zero
