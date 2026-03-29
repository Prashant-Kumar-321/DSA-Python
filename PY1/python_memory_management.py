"""
1. In Python Everything is Object
2. Object get memory in heap 
3. Reference variable get memory in stack and lives until stack-frame lives
4. Python is dynamically typed language and interpreted
5. Python maintains reference count of each object
6. Objects with 0 reference count is called Dead object and Garbage collector sweep it out from memory
7. Garbage collector algorithm is called Reference Counting

"""

x = 10 
print(type(x))

y = x
print(id(x), id(y))
if(id(x) == id(y)): 
    print('x and y refer to same object')

x += 1 # Create a new object with value 11 and assign reference to x
if(id(x) != id(y)): 
    print('x, and y does not refer same object')


z = 10 
if (id(z) == id(y)): 
    print('y, and z are refering same object')


class Car: 
    def __init__(self, wheel): 
        self.wheel = wheel
    
    def getWheel(self): 
        return self.wheel

z = Car(4)
print(type(z))

import weakref 

c1 = Car(8)
print(f"C1 Memory Location, {hex(id(c1))}")
wr = weakref.ref(c1) # does not increase reference count

print(f'before: {wr}')
c1 = None 
print(f"After : {wr}")



