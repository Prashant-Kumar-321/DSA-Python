from collections import deque

dq = deque([1, 2, 3])

# Add element
dq.append(4)        # add to right
dq.appendleft(0)    # add to left

# Remove elements
dq.pop()     # remove from right
dq.popleft() # remove left element

# Peek top elements
print(dq[0]) # Access left element
print(dq[-1]) # Access right element

print(dq)

# Shift right 
# dq.rotate(1)  # shift right
# dq.rotate(-1) # shift left

print(dq)


# ************* STACK (LIFO) *********
stack = deque()

stack.append(8) # insert right
stack.append(9)
stack.append(10)

print("Stack")
while stack: 
    top = stack.pop() # delete right
    print(top)

# ************* List as Stack *************
stack = list()
stack.append(67)
stack.append(90)
stack.append(54)

print("List Stack")
while stack: 
    top = stack.pop()
    print(top, end=" ")
print() 



# ************* QUEUE (FILO) **************** 
queue = deque()

queue.appendleft(9)
queue.appendleft(8)
queue.appendleft(7)

print('Queue')
while queue: 
    front = queue.pop()
    print(front)







