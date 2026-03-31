import sys 
sys.stdout = open('Array/output.txt', 'w')
sys.stdin = open('Array/input.txt', 'r')


def max_num(nums: list[int]) -> int:
    mx = float('-inf')

    for num in nums: 
        mx = max(mx, num)
    
    return mx

def second_maxmin(nums: list[int]) -> int: 
    max1, max2 = float('-inf'), float('-inf')
    min1, min2 = float('inf'), float('inf')

    for num in nums: 
        # find max elements
        if num > max1: 
            max2 = max1 
            max1 = num
        elif num > max2: 
            if num != max1: # guard max2 = max1
                max2  = num 
        
        # find min elements
        if num < min1: 
            min2 = min1 
            min1 = num 
        elif num < min2: 
            if num != min1: # guard min2 = min1
                min2 = num
    
    return max2, min2

if __name__  == "__main__": 
    nums = list(map(int, input().split()))

    # print(max_num(nums))
    print(second_maxmin(nums))


