# ESCAPE SEQUENCES; using a backslash to escape quotes e.g., what to do if you want quotation marks in your string.

# Adding whitespace to strings with tabs/new lines
print("\t Once upon a time")  # indicates indentation in string or creating tab

print("Python \nProgramming")  # indicates line break in string
print("This will \nbegin on a \nnew line")
print('Why should I be tarred with the epithet "loony" merely because I have a pet halibut.')
print("I think you\'re an encyclopaedia salesman")


print("Python \Programming")  # escape character
print("Python \\Programming")
print("Python \"Programming")  # escape sequence
print("Let's print a backslash: \\")

# wrapping string in its own pair of double quotes
print("\"To be or not to be\", said Hamlet")
print('Simon\'s skateboard is in the garage.')

# Creating raw string to avoid Python escaping slashes on file directories
file_name = r"C:\news\travel"
print(file_name)

# Backslash to break up line
some_random_number = 5
some_obscure_calculation = 25
some_additional_statistic_fetched_from_somewhere = 10

final = some_random_number + \
    some_obscure_calculation + \
    some_additional_statistic_fetched_from_somewhere

print(some_random_number,
      some_obscure_calculation,
      some_additional_statistic_fetched_from_somewhere)
