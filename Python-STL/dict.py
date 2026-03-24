# dict 
# key-value pair
# Key: Only immutable types

d = {"a": 1, "b": 2}
empty_d = {}

# Accessing values
print(d["a"])
print(d.get("a", "fallback value")) # safe way
print(d.get("c", "default value")) 

# adding / updating element
d["a"] = 10 # update value of key a
d["c"] = 3 # add key c

print(d)

# ******** Remove key ************ 
try: 
    del d["d"]
except KeyError as error: 
    print("Key does not present")

ret_value = d.pop("d", 'Default value')  # removes and returns value
print(ret_value)

print(d.popitem()) # remove and return last inserted value
print(d)

print("a" in d) # check if key present

# **** Looping through dictionary ******* 
# 1. Key 
for key in d: 
    print(key, end=" ")
print()

# 2. values 
for value in d.values(): 
    print(value, end=" ")
print()

# 3. key-value pairs
for key, value in d.items(): 
    print(key, value)
print()