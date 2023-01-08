# Stack is a linear data structure fllowing a particular order in which operations are performed; 
# Resembles stack of books; the last book you put on top of your stack is the first book that you can remove.
# LIFO or FILO (Last In Fist Out or First In Last Out)
# Real world example is a browser; whenever you navigate to a new website, your browser keeps your browsing section in a stack, so when you click on back button, it takes you to the previous website.

browsing_session = [] # define variable browsing_session and set it to an empty list 
browsing_session.append(1) # user navigates to website number 1; append method adds an item on top of the stack
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
# When user presses the back button, we should remove the last item in list, using pop method.
last = browsing_session.pop() # pop method removes item on top of stack
print(last) # 3 is removed from the stack.
print(browsing_session) # And we only have 2 items on our stack.
# Now, we need to take the user to the previous website which is the item on top of the stack. And we can get that using a -1 index.
print("redirect", browsing session[-1]) # index -1 to get item on top of the stack.
# Before getting item on top of the stack, check to see if the stack is empty or not. If it becomes empty, disable the back button.
if not browsing_session:
    print("disable")


browsing_session = []
browsing_session.append()
browsing_session.pop()
if not browsing_session:
    browsing_session[-1]