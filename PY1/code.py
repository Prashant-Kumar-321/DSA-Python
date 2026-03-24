import sys
sys.stdout = open('PY1/output.txt', 'w')
sys.stdin = open('PY1/input.txt', 'r')

n = int(input())

nums = map(int, input().split())

sum = 0 
for num in nums: 
    sum += num 


print(sum)
