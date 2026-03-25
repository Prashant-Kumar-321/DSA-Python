import sys 
sys.stdout = open('Math/output.txt', 'w')
sys.stdin = open('Math/input.txt', 'r')

def reverse(n): 
    rev = 0

    while n: 
        last_digit = n%10 # get last digit of number
        n //= 10 # remove the last digit
        rev = rev * 10 + last_digit

    return rev

def is_palindrome(n):
    return n == reverse(n)

# O(log10(N)) O(logN)

if __name__ == "__main__": 
    n = int(input())
    res = is_palindrome(n)
    print(res)

