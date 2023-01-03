dict() # Hash map / Map / Asociative array - unordered data structure for declaring relationships between objects
# A hash table is a data structure which stores in an associative manner. Data is stored in an array format, where each data value has its own unique index value.
# Dictionary is a collection that associates immutable keys with vaues of any type; coolection of key value pairs.
# key -> value; used to map a key to a value.
# e.g., In a phonebook; you map a person's name to contact details; 
# use a person's name as key and contact information as value.

# Phonebook - dictionary
# name(key) -> contact(value)
# In Python, we often use immutable types for keys(strings and numbers).
# Values can be of any type.

point = {"x": 1, "y": 2}
dict() # function that can be used to create a dictionary, put keyword arguments inside
point = dict(x=1, y=2) # Syntax a little bit cleaner and shorter.
# One can get the value associated with  key using an index; index is the name of the key.
# Instead of point[0], we do point[x].
# Because dictionaries are collections of key-value pairs, we cannot access an item using a numeric index as we do with lists.

# BASIC OPERATIONS IN DICTIONARIES
point["x"] = 10 # changing value of x to a new value.
point["z"] = 20 # adding a new key 

# Checking for existence of key
if "a" in point:
    print(point["a"])
#or
print(point.get("a")) # get method. If key doesn't exist, it returns None by default.

# Checking for existence of key and passing a default value as a 2nd argument
print(point.get("a", 0)) # If we don't have an item with key a, return 0 by default.

# Deleting an item; del/ delete statement
del point["x"]
print(point)

# How to loop over/ iterate over dictionaries
