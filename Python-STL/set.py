s = {2, 7, 8}
nums = set() # create an empty set

s.add(6) # Add an element in the set
s.update([0, 1, 4, 5]) # add multiple elements
print(s)

try: 
    s.remove(3)
except KeyError as error: 
    print("element not present")

s.discard(3) # No error if ele not found
ret_element = s.pop() # remove random element
# s.clear() # remove all 

print(s)

print(2 in s) # look up very fast O(1) average time


# ********* Set Operations *********
a = {1, 2, 3}
b = {3, 4, 5}

print(a|b) # union 
print(a.union(b))

print(a&b) # intersection
print(a.intersection(b))

print(a-b) # difference
print(a.difference(b))

print(a^b) # Symmetric Difference - not common 

print(len(s))

new_s = s.copy()
print(new_s)

# create list of unique elements
arr = [3, 5, 7, 3, 7, 1, 3, 6]
unique = list(set(arr)) 
unique.sort()
print(f"Unique elements = {unique}")

# frozenset (immutable set)
fs = frozenset([3, 5, 8, 1, 3])
print(f"frozen set = {fs}")
