# 🚀 Key Takeaways
    # Tuple = immutable list (Once created can not be changed)
    # Faster than list (slightly)
    # Safe for fixed data
    # Useful in hashing (dict/set keys)

t = (3, 4, 8)
single_t = (6,) # important (comma required)
empty_t = () # empty

# Accessing elements
print(t[0], end=" ") # 3
print(t[2], end=" ") # 8
print(t[-2],) # 4 

# Iterate through tuple
for te in t: 
    print(te, end=" ")
print()

# Slicing 
tup = ("A", "B", "C", "D", "E", "F")
print(tup[1:4]) # ("B", "C", "D")
print(tup[:3]) # (A, B, C)
print(tup[:]) # (A, B, C, D) 

# Repetition
t = (1, 2)
print(t*2)

# Membership check
print(5 in t) # True

# Packing & Unpacking (Important)
pair = 5, 9 # Packing
print(type(pair))
x, y = pair # Unpacking
print(x, y)

a, *b = (1, 7, 9, 5)
# a = 1, b = [7, 9, 5]
print(a, b)

# Nested Tuples
coordinates = ((1, 2), (5, 7))
bottom_left, top_right = coordinates
print(bottom_left, top_right)

# Swap values of two variables
a, b = 5, 10 
print(f"Before swapping, a = {a}, b = {b}")

b, a = a, b

print(f"After swapping, a = {a}, b = {b}")






