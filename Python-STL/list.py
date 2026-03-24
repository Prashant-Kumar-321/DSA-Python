arr = [1, 2, 3, 4, 5]

# ********** Accessing element by index *************** 
# print(arr[0])
# print(arr[1])
# print(arr[-1]) # last element
# print(arr[-len(arr)])

# ***** Iterate over list through index **************
# n = len(arr)
# for i in range(n): 
#     print(arr[i], end=" ")

# for ele in arr: 
#     print(ele, end="")

# ********** Add elements ************ 
arr.append(6) # add element at the end 
arr.insert(2, 9) # insert at specific index
arr.extend([10, 11, 12]) # add multiple elements at the end
print(arr)

# ************* Delete elements **************
arr.remove(6) # remove by first element
arr.pop() # remove last element
ret_ele = arr.pop(2) # remove by index
print(f"return element = {ret_ele}")
arr.clear() # remove all elements
print(arr)

# ******* update list *************** 
games = ["Mario", "Temple Run", "Bubble", "Pubgi 5", "Sudoko"]
games[0] = "Strong Mario"
# print(games[5]) # list index out of range exception occurs
print(games[0])

# ************* Slicing (Sub-List) ***************
nums = [3, 4, 7, 9, 0, 10]
print(nums[:3]) # [3, 4, 7]
print(nums[4:]) # [0, 10]
print(nums[:]) # whole list [3, 4, 7, 9, 0, 10]
print(nums[::2]) # return list of every second element

# **************** Searching ******************
num = 19
if num in nums: 
    print(f"{num} is present in the list")
else: 
    print(f"{num} is not present in the list")


# ************* get index of element **************** 
try: 
    idx = nums.index(20)
    print(idx)
except ValueError as err: 
    print("Value is not present in the list")

print(len(nums))

print(nums)

# ************* sort list ********************

# 1. modify original list
# nums.sort()
# nums.sort(reverse=True)

# 2. return sorted list
# az = sorted(nums)
# za = sorted(nums, reverse=True)
# print(nums)
# print(az, za)

# **************** reverse list *****************
nums.reverse()
print(nums)

print(nums.count(0))

# ***************** list comprehension ***********
squares = [x*x for x in range(1, 6, 1)]
print(squares)

# ************* Copying a list *******************
new_nums = nums.copy()
new_nums[0] = 5
print(new_nums)

# ********** Concatenate two lists **************
ages_classA = [15, 12, 15, 17]
ages_classB = [18, 13, 15, 16]

ages_classAB = ages_classA + ages_classB 

print(f"class A = {ages_classA}")
print(f"class B = {ages_classB}")
print(f"class AB = {ages_classAB}")


# *********** Sorting with custom key ****************
nums = [(3, 5), (9, 2), (0, 3), (10, 21), (0, 2)]
nums.sort(key=lambda x: x[1])
print(nums)

