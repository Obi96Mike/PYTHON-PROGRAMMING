# Loops that run forever. 
# You should always jump out of them otherwise your program will run forever.
# This can cause issues because if you are executing operations that consume memory, at some point your program may run out of memory and crash.
# Use break statement/ keyword
command = ""
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() = "quit":
        break


while True:
    num = input("Enter an integer: ")
    if num.isdigit():
        break