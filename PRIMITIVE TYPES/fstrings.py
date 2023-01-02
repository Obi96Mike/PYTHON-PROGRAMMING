# Allows us to directly interpolate variables or expressions into a string.
# Useful way to build a string containing variables and expressions inside of them.

first = "Obi"
last = "Mike"

full = first + " " + last  # String Concatenation
print(full)
full_name = f"{first} {last}"  # f-string
print(full_name)

# Valid expressions
valid_exp = f"{len(first)} {last}"
valid_expr = f"{len(first)} {2+2}"

name = "Obi"
adjective = "green"
noun = "alien"
full_sentence = f"{name} laughed at the {adjective} {noun}"
print(full_sentence)

# Mathematical expression
print(f"2+2 is {2+2}")


name = input("Name: ")
sentence = f"Hello, {name}! Thanks!"  # f-string
print(sentence)
full_sen = "Hello,", name + "!Thanks!"  # Concatenation
print(full_sen)
