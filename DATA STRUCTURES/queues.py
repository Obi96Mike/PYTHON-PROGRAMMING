# A linear data structure which is open at both ends and operations are performed in FIFO order. The element which is first pushed into order, the operation is first performed on that
# Queue of people to get into a restaurant; first person in queue is the first person being served.
# FIFO
# [1, 2, 3]
# Technically, you can use a list to implement a Queue in Python. If you want to remove an item from the queue, remove the one at the beginning, 1 , then 2, then 3.
# However, if you're dealing with a large list/ queue, you might see some adverse effect on the performance.
# e.g., if you have a large number of items in the list, everytime you remove an item from beginning of this list, all the other items need to be shifted to the left.
# If you have a list of 1001 items, when you remove 1 item, 1000 items need to be moved in memory.
# In situations like this, more efficient to use deque object which has similar methods that we have in list object.

from collections import deque # import deque class from collections module; module is a bucket with a bunch of reusable code.
queue = deque([]) # Instead of defining a variable and setting it to an empty list, we wrap it with a deque object. We call deque and pass an empty list as an argument.
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft() # to remove an item from beginning of queue, call queue.popleft
print(queue)
# Similar to lists, we can easily check to see if queue is empty using not operator.
if not queue:
    print("empty")