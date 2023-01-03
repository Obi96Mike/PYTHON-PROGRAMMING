# While loop is used to repeat something as long as condtion is True.
# If you don't know how many times you want to loop, use a while loop.
# Anything that can be done with a for loop can also be done with a while loop.

# count from 0-5 application
count = 0
while count <= 5:
    print(count)
    count += 1

for x in range(5):
    print(x)
    
# counting.py
current_number = 1
while current_number <=5:
    print(current_number)
    current_number += 1


# If you know how many times you want to loop, use a for loop.
for x in range(5):
    print(x)


# Enter a program that asks the user to enter an integer.
# While the number is not a digit, keep asking the user to enter an integer.


# num = input("Enter an integer: ")
# while not num.isdigit():
    # num = input("Enter an integer: ")

  
# break keyword
while True:
    num = input("Enter an integer: ")
    if num.isdigit():
        break


# Looping through a list
# Breaking while loop as soon as sum of numbers added in list is >9
lst = [2, 3, 3, 2, 2, 1]

result = 0 # storing sum of values in list
i = 0 # keeps track of current index

while result < 9 and i < len(lst):
    num = lst[i]
    result += lst[i]
    i +=1

    print(num)


# While Else 
lst = [2, 3, 3, -2, -2, -1]
i = 0

while i < len(lst):
    if lst[i] == -2:
        print("Found it")
        break
    else:
        print("Didn't find it ")

# Write a program that continually asks the user to enter a number until they enter number 5, at which point the program should print how many nume=bers the user has entered.
# You may assume the user will only enter a number.
number_of_entries = 0

while True:
    number = int(input("Enter a number: "))
    number_of_entries += 1

    if number == 5:
        break

print(f"You entered {number_of_entries} numbers.")



# Write a program that continually asks the user to enter a word until they enter the word "q" or "quit,"
# at which point the program should print the average length of all the entered words excluding the "q" or "quit."
# If the user doesn't enter any words (immediately enters "q" or "quit"), your program shouldn't print anything.

word_length_sum = 0 
word_count = 0

while True:
    word = input("Enter a word: ")

    if word == "q" or word == "quit":
        break

    word_length_sum += len(word)
    word_count += 1

if word_count > 0:
    average_word_length = word_lenghth_sum / word_count
    print(f"The average word length is: {average_word_length}.")

#or
words = []

while True:
    word = input("Enter a word: ")

    if word == "q" or word == "quit":
        break

    words.append(word)

if len(words) > 0:
    word_length_sum = 0

    for word in words:
        word_length_sum += len(word)

    average_word_length = word_length_sum / len(words)
    print(f"The average word length is: {average_word_length}.")


# Use a while loop to print the squares of the numbers 1, 3, 6, 10, 15 and 21.
nums = [1, 3, 6, 10, 15, 21]
idx = 0

while idx < len(nums):
        num = nums[idx]
        print(num * num )

        idx +=1