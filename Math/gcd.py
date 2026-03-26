import sys 
sys.stdout = open('Math/output.txt', 'w')
sys.stdin = open('Math/input.txt', 'r')

def gcd(a:int, b:int)->int: 
    """Calculate GCD value of a and b"""
    if a < b: 
        a, b = b, a
    
    while b != 0: 
        temp = a % b
        a = b 
        b = temp 
    
    return a

def gcd(a:int, b:int)->int:
    """Recursive defintion of euclid gcd algorithm"""
    if b == 0: return a 
    return gcd(b, a%b)

def is_armstrong(x:int) -> bool: 
    """
    Armstrong #: sum of digits each raised to power of number of digits
    """

    def count_digits(x:int) -> int:
        cnt = 0 
        while x: 
            cnt += 1
            x //= 10
            
        return cnt 

    d_cnt = count_digits(x) # O(log(x))
    d_cnt = len(str(x)) # O(log(x))
    arm = 0
    temp = x

    while temp: 
        pop = temp%10
        arm += pop ** d_cnt
        temp //= 10

    return arm == x

# TC: O(log^2(x))

# Time Complexity Analyse later

if __name__ == "__main__": 
    # a,b = map(int, input().split())
    # res = gcd(a, b)

    x = int(input())
    res = is_armstrong(x)

    print(res)

