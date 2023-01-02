# STRINGS - data type for immutable 0 or more sequence of characters that are connected together; consisting of letters, numbers, symbols, spaces.
# str data type  in Python starts and ends with single, double or triple quotes - '', "", """"""

# single or double quotes
course_name = 'Python programming'
course_name = "Python programming"

# triple quotes (multiline strings)
message = """
Hi John,

This is Mike from obimike.com
Thank you.
"""
print(message)

# STRING CONCATENATION - using + sign to combine together 2 strings.
print("Ba" + "con")
print("Obi " + "Mike")
print("Obi" + " Mike")
print("Obi" + " " + "Mike")
first_word = "Hello"
second_word = "there"
print(first_word + second_word)

# String Multiplication - It repeats the string as many times as you multiply it.
print("---" * 30)


# STRING INDEXING
# [] square bracket notation - getting access to a specific character or element in a string.
course = "Python programming"
print(course[0])  # to get first character in a string.
