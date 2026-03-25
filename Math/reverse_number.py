import sys 
sys.stdout = open('Math/output.txt', 'w')
sys.stdin = open('Math/input.txt', 'r')

def reverse_number(n):
    rev = 0

    while n: 
        last_digit = n%10 # get last digit of number
        n //= 10 # remove the last digit
        rev = rev * 10 + last_digit

    return rev

# O(log10(N)) O(logN)

if __name__ == "__main__": 
    n = int(input())
    res = reverse_number(n)
    print(res)